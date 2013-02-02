// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Factory class so that all servlets and classes in this application will use
 * the same algorithms (ex. RandomForest).
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public class Factory {
  private static LearningModelFactory factory;
  private static LearningIterFactory iterFactory;

  public static LearningModelFactory getFactory() {
    if (factory == null) {
      factory = new ForestModelFactory();
    }
    return factory;
  }

  public static LearningIterFactory getIterFactory() {
    if (iterFactory == null) {
      iterFactory = new ForestIterFactory();
    }
    return iterFactory;
  }
  private Factory() {}
}
