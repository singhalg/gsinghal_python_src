// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.IOException;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.appengine.api.datastore.PreparedQuery;
import com.google.appengine.api.datastore.Query;
import com.google.appengine.api.datastore.Text;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * Servlet to print the decision of the learning algorithm.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class DecisionViewServlet extends RemoteServiceServlet {

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    System.out.println("Decision view servlet started!");

    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();

    Query q = new Query("Decision");

    PreparedQuery pq = datastore.prepare(q);

    ServletOutputStream os = res.getOutputStream();
    ArrayList<String> clazzes = new ArrayList<String>();
    ArrayList<Float> decisions = new ArrayList<Float>();
    boolean firstPass = true;
    for (Entity result : pq.asIterable()) {
      String decision = ((Text)result.getProperty("decision")).getValue();
      String decisionStrings[] = decision.split("\n");
      int length = decisionStrings.length;
      for (int i = 0; i < length; ++i) {
        String[] ds = decisionStrings[i].split(",");
        String clazz = ds[0];
        String decisionString = ds[1];
        float d = Float.parseFloat(decisionString);
        if (firstPass) {
          clazzes.add(clazz);
          decisions.add(d);
        } else {
          decisions.set(i, decisions.get(i) + d);
        }
      }
      firstPass = false;
      os.print("Decision:\n");
      int size = clazzes.size();
      for (int i = 0; i < size; ++i) {
        os.print(clazzes.get(i) + ": " + decisions.get(i) + "\n");
      }
    }

    System.out.println("Decision view servlet terminating!");
  }
}