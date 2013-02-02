// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.appengine.api.backends.BackendService;
import com.google.appengine.api.backends.BackendServiceFactory;
import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.appengine.api.datastore.FetchOptions;
import com.google.appengine.api.datastore.PreparedQuery;
import com.google.appengine.api.datastore.Query;
import com.google.appengine.api.datastore.Transaction;
import com.google.appengine.api.taskqueue.Queue;
import com.google.appengine.api.taskqueue.QueueFactory;
import com.google.appengine.api.taskqueue.TaskOptions;
import com.google.appengine.api.taskqueue.TaskOptions.Method;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * Servlet for queuing tests.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class RunTestServlet extends RemoteServiceServlet {

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    System.out.println("Frontend started!");

    ServletOutputStream os = res.getOutputStream();

    Object kObject = req.getParameter("k");
    if (kObject == null) {
      os.print("No k specified!");
      return;
    }
    int k = (Integer.parseInt(kObject.toString()));

    Object masterSeedObject = req.getParameter("masterSeed");
    if (masterSeedObject == null) {
      os.print("No masterSeed specified!");
      return;
    }
    int masterSeed = (Integer.parseInt(masterSeedObject.toString()));

    DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
    Query q = new Query(Constants.DATASET);
    q.addFilter("masterSeed", Query.FilterOperator.EQUAL, masterSeed);
    PreparedQuery pq = datastore.prepare(q);
    int count = pq.countEntities(FetchOptions.Builder.withDefaults());
    System.out.println("count: " + count);
    String[] seeds = new String[count];
    int entityIndex = 0;
    int seedsIndex = 0;
    for (Entity entity : pq.asIterable()) {
      //System.out.println("entity: " + entity.toString());
      //System.out.println("entityIndex: " + entityIndex);
      //System.out.println("entityIndex % 10: " + (entityIndex % 10));
      if (entityIndex % Constants.FORESTS_PER_SHARD == 0) {
        System.out.println("seedsIndex: " + seedsIndex);
        ++seedsIndex;
        System.out.println("seedsIndex: " + seedsIndex);
        seeds[seedsIndex - 1] = "";
      }
      seeds[seedsIndex - 1] += entity.getProperty("seed") + ",";
      ++entityIndex;
    }

    Queue queue = QueueFactory.getDefaultQueue();
    BackendService backendsApi = BackendServiceFactory.getBackendService();
    String backendAddress = backendsApi.getBackendAddress("worker");
    System.out.println("workder address: " + backendAddress);
    int currentTask = 0;
    System.out.println("seedsIndex: " + seedsIndex);
    while (currentTask < seedsIndex) {
      int counter = 0;
      Transaction txn = datastore.beginTransaction();
      ArrayList<TaskOptions> tasks = new ArrayList<TaskOptions>(seedsIndex);
      while (counter < 5 && currentTask < seedsIndex) {
          TaskOptions taskOptions =
              TaskOptions.Builder.withUrl(
                  "/testing?" +
                      "&k=" + k +
                      "&masterSeed=" + masterSeed +
                      "&seeds=" + seeds[currentTask])
                      .method(Method.GET);
          taskOptions.header("host", backendAddress);
          tasks.add(taskOptions);
          ++counter;
          ++currentTask;
      }
      queue.add(txn, tasks);
      txn.commit();
      try {
        Thread.sleep(100);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }

    System.out.println("Frontend terminating!");
  }
}