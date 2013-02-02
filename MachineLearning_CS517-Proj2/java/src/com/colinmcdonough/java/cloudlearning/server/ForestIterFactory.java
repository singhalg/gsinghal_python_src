// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Factory for RandomForest's ForestIter.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public class ForestIterFactory implements LearningIterFactory {

  @Override
  public ForestIter getIter(int numTrees, int maxDepth, int seed,
      double branching, Dataset dataset) {
    return ForestIter.getForestIter(numTrees, maxDepth, seed, branching, dataset);
  }

}
