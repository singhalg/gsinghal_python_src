// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Implementation of a LearnedModelFactory for forests of trees.
 * @author cmcdonough
 *
 */
public class ForestModelFactory implements LearningModelFactory {

  @Override
  public LearningModel fromSeedsAndWeights(int seed, float[] weights) {
    return ForestModel.fromSeedsAndWeights(seed, weights);
  }
  
  @Override
  public LearningModel fromString(String string) {
    return ForestModel.fromString(string);
  }

}
