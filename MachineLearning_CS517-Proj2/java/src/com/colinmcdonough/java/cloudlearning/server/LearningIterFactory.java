// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Inteface for IterFactories.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public interface LearningIterFactory {
  
  public LearningIter getIter(int numTrees, int maxDepth, int seed,
      double branching, Dataset dataset);
}
