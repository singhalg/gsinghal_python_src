// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.appengine.api.datastore.FetchOptions;
import com.google.appengine.api.datastore.Key;
import com.google.appengine.api.datastore.KeyFactory;
import com.google.appengine.api.datastore.PreparedQuery;
import com.google.appengine.api.datastore.Query;
import com.google.appengine.api.datastore.Text;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * Servlet for running tests over test data using a previously generated model.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class ForestTestServlet extends RemoteServiceServlet {

  private static final Logger LOG = Logger.getLogger(ForestTestServlet.class.getName());

  private final static int COMMA = (int) ',';
  private final static int NEWLINE = (int) '\n';
  
  private LearningModelFactory factory;
  private final LearningIterFactory iterFactory;
  
  public ForestTestServlet() {
    factory = Factory.getFactory();
    iterFactory = Factory.getIterFactory();
  }

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    LOG.info("Testing backend started!");
    System.out.println("Testing backend started!");

    ServletOutputStream os = res.getOutputStream();
    Object kObject = req.getParameter("k");
    if (kObject == null) {
      os.print("No k specified!");
      LOG.severe("No k specified!");
      return;
    }
    Object masterSeedObject = req.getParameter("masterSeed");
    if (masterSeedObject == null) {
      os.print("No masterSeed specified!");
      LOG.severe("No masterSeed specified!");
      return;
    }
    LOG.info("masterSeed=" + masterSeedObject.toString());
    Object seedsObject = req.getParameter("seeds");
    if (seedsObject == null) {
      os.print("No seeds specified!");
      LOG.severe("No seeds specified!");
      return;
    }

    Dataset dataset = new Dataset();
    ServletContext context = getServletContext();
    InputStream is = context.getResourceAsStream("/WEB-INF/dataset/dataset.csv");
    int attributeCount = 0;
    int b = 1;
    while ((b = is.read()) != NEWLINE) {
      if (b == COMMA) {
        ++attributeCount;
      }
    }
    BufferedReader reader = new BufferedReader(new InputStreamReader(is));
    reader.readLine();
    String line;
    char[] buff = new char[10];
    int buffPos = 0;
    b = 0;
    boolean isClazz = true;
    String clazz = "bad_class";
    int[] attributes = new int[attributeCount];
    int[] mins = new int[attributeCount];
    int[] maxes = new int[attributeCount];
    int attributeIndex = 0;
    while (reader.ready()) {
      while ((b = reader.read()) != COMMA && b != NEWLINE) {
        buff[buffPos] = (char) b;
        ++buffPos;
      }
      if (isClazz) {
        char[] classChar = new char[buffPos];
        System.arraycopy(buff, 0, classChar, 0, buffPos);
        clazz = new String(classChar);
        isClazz = false;
      } else {
        char[] attributeChar = new char[buffPos];
        System.arraycopy(buff, 0, attributeChar, 0, buffPos);
        attributes[attributeIndex] =
            (int) (Float.parseFloat(new String(attributeChar)) * 10);
        mins[attributeIndex] = Math.min(attributes[attributeIndex], mins[attributeIndex]);
        maxes[attributeIndex] = Math.max(attributes[attributeIndex], maxes[attributeIndex]);
        if (b == COMMA) {
          ++attributeIndex;
        } else if (b == NEWLINE) {
          dataset.addEntry("id", clazz, attributes);
          // Make a new object to avoid mutating it.
          attributes = new int[attributeCount];
          isClazz = true;
          attributeIndex = 0;
        }
      }
      buffPos = 0;
    }
    dataset.setRanges(mins, maxes);

    LOG.info("Forest (re)created");

    // Read in test data.

    is = context.getResourceAsStream("/WEB-INF/dataset/test.csv");
    reader = new BufferedReader(new InputStreamReader(is));
    //reader.readLine();
    line = reader.readLine();
    //String clazz = values[0];
    ArrayList<Integer[]> attributesList = new ArrayList<Integer[]>();
    ArrayList<String> clazzes = new ArrayList<String>();

    while ((line = reader.readLine()) != null) {
      String[] values = line.split(",");
      int length = values.length;
      clazzes.add("?");
      Integer[] a = new Integer[length];
      for (int i = 0; i < length; ++i) {
        int attribute = (int) (Float.parseFloat(values[i]) * 10);
        a[i] = attribute;
      }
      attributesList.add(a);
    }

    int k = (Integer.parseInt(kObject.toString()));
    int masterSeed = (Integer.parseInt(masterSeedObject.toString()));
    String[] seeds = seedsObject.toString().split(",");
    System.out.println("seedsObject.toString -> " + seedsObject.toString());
    int l = seeds.length;
    for (int i = 0; i < l; ++i) {
      System.out.println("seeds[" + i + "] -> " + seeds[i]);
    }
    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
    Query q = new Query(Constants.DATASET);
    q.addFilter("masterSeed", Query.FilterOperator.EQUAL, masterSeed);
    List<String> seedsStrings = Arrays.asList(seeds);
    List<Integer> seedIntegers = new ArrayList<Integer>(seedsStrings.size());
    for (String s : seedsStrings) {
      seedIntegers.add(Integer.parseInt(s));
    }
    q.addFilter("seed", Query.FilterOperator.IN, seedIntegers);
    PreparedQuery pq = datastore.prepare(q);
    int attributesListSize = attributesList.size();
    float[] decision = new float[attributesListSize];
    List<Entity> entities = pq.asList(FetchOptions.Builder.withDefaults());
    List<LearningModel> treeSets = new ArrayList<LearningModel>(entities.size());
    for (Entity entity : entities) {
      LearningModel treeSet =
          factory.fromString(((Text) entity.getProperty(Constants.DATAPROPERTY)).getValue());
      treeSets.add(treeSet);
    }
    for (LearningModel treeSet : treeSets) {
      float[] weights = treeSet.getWeights();
      LearningIter forest = iterFactory.getIter(k, Constants.MAX_DEPTH, treeSet.getSeed(), Constants.BRANCHING, dataset);
      int forestSize = forest.size();

      int attributesLength = attributesList.get(0).length;
      int[][] attributesArray = new int[attributesListSize][attributesLength];
      for (int i = 0; i < attributesListSize; ++i) {
        Integer[] list = attributesList.get(i);
        for (int j = 0; j < attributesLength; ++j) {
          attributesArray[i][j] = list[j];
        }
      }
      
      for (int i = 0; i < forestSize; ++i) {
        // Test each patient
        if (Math.abs(weights[i]) > 0.4) {
          for (int j = 0; j < attributesListSize; ++j) {
            clazz = forest.decide(attributesArray[j]);
            if (clazz.equals(Forest.CLASS_ALZHIEMERS)) {
              //System.out.println("a");
              decision[j] += weights[i];
            } else if (clazz.equals(Forest.CLASS_NOT_ALZHIEMERS)) {
              //System.out.println("a");
              decision[j] -= weights[i];
            } else {
              LOG.severe("ERROR: class is \"" + clazz + "\"");
            }
          }
        } else {
          System.out.println("Skipping tree with weight " + weights[i]);
        }
        if (i % 100 == 0) {
          LOG.info("Evaluating with tree (" + i + "/" + (forestSize - 1) + ")");
        }
        if (!forest.hasNext()) {
          break;
        }
        forest.next();
      }
    }
    StringBuffer decisionBuffer = new StringBuffer();
    int length = attributesList.size();
    for (int i = 0; i < length; ++i) {
      String d = clazzes.get(i) + ","+ decision[i] + "\n";
      System.out.println(d);
      decisionBuffer.append(d);
    }
    Key decisionSetKey = KeyFactory.createKey("Decision", k);
    Entity decisionEntity = new Entity("Decision", decisionSetKey);
    decisionEntity.setProperty("masterSeed", masterSeed);
    decisionEntity.setProperty("decision", new Text(decisionBuffer.toString()));
    datastore.put(decisionEntity);

    LOG.info("Testing backend terminating!");
    System.out.println("Testing backend terminating!");
  }
}