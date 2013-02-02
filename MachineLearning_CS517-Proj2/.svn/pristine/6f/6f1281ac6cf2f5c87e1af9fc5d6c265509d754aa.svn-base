// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.util.List;

/**
 * Interface for iterating over a learned model.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public interface LearningIter {

  public boolean hasNext();

  void next();

  public String decide(int[] attributes);

  float[] evaluateForest(Dataset dataset);

  List<Integer> getFeatures();

  int size();

}
