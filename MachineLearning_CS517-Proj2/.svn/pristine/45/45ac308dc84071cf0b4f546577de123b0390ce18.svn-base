// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.IOException;
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
 * Servlet to display the contents of the Datastore.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class DatastoreViewServlet extends RemoteServiceServlet {

  private LearningModelFactory factory;

  public DatastoreViewServlet() {
    factory = Factory.getFactory();
  }

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    System.out.println("Servlet started!");

    ServletOutputStream os = res.getOutputStream();

    Object masterSeedObject = req.getParameter("masterSeed");
    if (masterSeedObject == null) {
      os.print("No master seed specified!");
      System.out.println("No master seed specified!");
      return;
    }
    int masterSeed = (Integer.parseInt(masterSeedObject.toString()));

    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();

    Query q = new Query(Constants.DATASET);
    q.addFilter("masterSeed", Query.FilterOperator.EQUAL, masterSeed);

    PreparedQuery pq = datastore.prepare(q);
    for (Entity result : pq.asIterable()) {
      LearningModel treeSet =
          factory.fromString(((Text)result.getProperty(Constants.DATAPROPERTY)).getValue());
      os.print("averageWeight: " + treeSet.getAverageWeight() +
          ", treeSet: " +
          treeSet.getWeight(0) + "\n" +
          treeSet.toDisplayString() + "\n");
    }

    System.out.println("Servlet terminating!");
  }
}