// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Interface for learned models.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public interface LearningModel {

  public float getAverageWeight();

  public float getWeight(int i);

  public String toDisplayString();
  
  public float[] getWeights();
  
  public int getSeed();
}
