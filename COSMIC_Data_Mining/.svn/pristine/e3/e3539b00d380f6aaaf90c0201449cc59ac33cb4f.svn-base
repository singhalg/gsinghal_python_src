// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.appengine.api.datastore.Key;
import com.google.appengine.api.datastore.KeyFactory;
import com.google.appengine.api.datastore.Text;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * Servlet to process a Dataset and generate a model.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class BackendServlet extends RemoteServiceServlet {

  private final static int COMMA = (int) ',';
  private final static int NEWLINE = (int) '\n';

  private Dataset dataset = null;
  Object datasetLock = new Object();
  
  private final LearningModelFactory factory;
  private final LearningIterFactory iterFactory;

  public BackendServlet() {
    factory = Factory.getFactory();
    iterFactory = Factory.getIterFactory();
  }

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    System.out.println("Backend started!");

    ServletOutputStream os = res.getOutputStream();

    Object masterSeedObject = req.getParameter("masterSeed");
    Object seedObject = req.getParameter("seed");
    Object kObject = req.getParameter("k");
    if (masterSeedObject == null) {
      os.print("No master seed specified!");
      System.out.println("No master seed specified!");
      return;
    }
    if (seedObject == null) {
      os.print("No seed specified!");
      System.out.println("No seed specified!");
      return;
    }
    if (kObject == null) {
      os.print("No k specified!");
      System.out.println("No k specified!");
      return;
    }

    if (dataset == null) {
      synchronized(datasetLock) {
        if (dataset == null) {
          Dataset privateDataset = new Dataset();
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
                privateDataset.addEntry("id", clazz, attributes);
                // Make a new object to avoid mutating it.
                attributes = new int[attributeCount];
                isClazz = true;
                attributeIndex = 0;
              }
            }
            buffPos = 0;
          }
          reader = null;
          is = null;
          context = null;
          attributes = null;
          privateDataset.setRanges(mins, maxes);

          System.out.println("dataset computed");
          dataset = privateDataset;
        }
        datasetLock.notifyAll();
      }
    } else {
      System.out.println("dataset precomputed");
    }

    int masterSeed = (Integer.parseInt(masterSeedObject.toString()));
    int seed = (Integer.parseInt(seedObject.toString()));
    int k = (Integer.parseInt(kObject.toString()));
    LearningIter forest = iterFactory.getIter(k, Constants.MAX_DEPTH, seed, Constants.BRANCHING, dataset);
    float[] weights = forest.evaluateForest(dataset);
    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
    Key treeSetKey = KeyFactory.createKey(Constants.DATASET, seed);
    Entity trees = new Entity(Constants.DATASET, treeSetKey);
    trees.setProperty("masterSeed", masterSeed);
    trees.setProperty("seed", seed);
    trees.setProperty(Constants.DATAPROPERTY, new Text(factory.fromSeedsAndWeights(seed, weights).toString()));
    datastore.put(trees);

    System.out.println("Backend terminating!");
  }
}