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
 * Servlet to combine multiple test results into one.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class CombineTestServlet extends RemoteServiceServlet {

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    System.out.println("Frontend started!");

    ServletOutputStream os = res.getOutputStream();

    Object masterSeedObject = req.getParameter("masterSeed");
    if (masterSeedObject == null) {
      os.print("No masterSeed specified!");
      return;
    }
    int masterSeed = (Integer.parseInt(masterSeedObject.toString()));

    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
    Query q = new Query("Decision");
    q.addFilter("masterSeed", Query.FilterOperator.EQUAL, masterSeed);
    PreparedQuery pq = datastore.prepare(q);
    ArrayList<String> clazzes = new ArrayList<String>();
    ArrayList<Float> decisions = new ArrayList<Float>();
    boolean firstTime = true;
    int index = 0;
    for (Entity entity : pq.asIterable()) {
      String[] pairs = ((Text)entity.getProperty("decision")).getValue().split("\n");
      for (String pair : pairs) {
        String[] s = pair.split(",");
        if (firstTime) {
          clazzes.add(s[0]);
          decisions.add(Float.parseFloat(s[1]));
        } else {
          decisions.set(index, Float.parseFloat(s[1]) + decisions.get(index));
        }
      }
      ++index;
      firstTime = false;
    }

    // output the data
    int length = clazzes.size();
    for (int i = 0; i < length; ++i) {
      os.print(clazzes.get(i) + "," + decisions.get(i) + "\n");
    }
    System.out.println("Frontend terminating!");
  }
}