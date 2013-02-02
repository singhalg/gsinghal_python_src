// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.appengine.api.backends.BackendService;
import com.google.appengine.api.backends.BackendServiceFactory;
import com.google.appengine.api.datastore.DatastoreFailureException;
import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Transaction;
import com.google.appengine.api.taskqueue.Queue;
import com.google.appengine.api.taskqueue.QueueFactory;
import com.google.appengine.api.taskqueue.TaskOptions;
import com.google.appengine.api.taskqueue.TaskOptions.Method;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * Servlet for queuing tasks which will learn the model.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
@SuppressWarnings("serial")
public class StartServlet extends RemoteServiceServlet {

	@Override
	public void doGet(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		System.out.println("Backend started!");

		ServletOutputStream os = res.getOutputStream();

		Object masterSeedObject = req.getParameter("masterSeed");
		Object nObject = req.getParameter("n");
		Object kObject = req.getParameter("k");
		if (masterSeedObject == null) {
			os.print("No master seed specified!");
			return;
		}
		if (nObject == null) {
			os.print("No n specified!");
			return;
		}

		if (kObject == null) {
			os.print("No k specified!");
			return;
		}
		int masterSeed = Integer.parseInt(masterSeedObject.toString());
		int n = (Integer.parseInt(nObject.toString()));
		int k = (Integer.parseInt(kObject.toString()));
		Random random = new Random(masterSeed);
		DatastoreService ds = DatastoreServiceFactory.getDatastoreService();
		Queue queue = QueueFactory.getDefaultQueue();
		BackendService backendsApi = BackendServiceFactory.getBackendService();
		String backendAddress = backendsApi.getBackendAddress("worker");
		System.out.println("workder address: " + backendAddress);
		try {
			int currentTask = 0;
			while (currentTask < n) {
				int counter = 0;
				Transaction txn = ds.beginTransaction();
				ArrayList<TaskOptions> tasks = new ArrayList<TaskOptions>(n);
				while (counter < 5 && currentTask < n) {
	                int seed = ~random.nextInt();
					TaskOptions taskOptions =
							TaskOptions.Builder.withUrl(
									"/_ah/start?" +
											"masterSeed=" + masterSeed +
											"&seed=" + seed +
											"&k=" + k)
											.method(Method.GET);
					taskOptions.header("host", backendAddress);
					tasks.add(taskOptions);
					++counter;
					++currentTask;
				}
				queue.add(txn, tasks);
				txn.commit();
			}
		} catch (DatastoreFailureException e) {
			e.printStackTrace();
		}

		System.out.println("Backend terminating!");
	}
}