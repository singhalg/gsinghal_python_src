// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Interface for LearnedModel factories.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public interface LearningModelFactory {
  public abstract LearningModel fromSeedsAndWeights(int seed, float[] weights);
  public abstract LearningModel fromString(String s);
}
