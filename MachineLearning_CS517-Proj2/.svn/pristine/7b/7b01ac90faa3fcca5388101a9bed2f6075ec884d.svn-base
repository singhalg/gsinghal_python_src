// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

/**
 * Implementation of LearnedModel for a forest of trees.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public class ForestModel implements LearningModel {

  private final static String COMMA = ",";
  private final static String NEWLINE = System.getProperty("line.separator");
  private final static int NUMBER_LENGTH = 2;

  private int seed;
  private float[] weights;

  private ForestModel() {}

  static public ForestModel fromString(String s) {
    ForestModel treeSet = new ForestModel();
    int length = s.length() / NUMBER_LENGTH;
    float[] weights = new float[length - 1];
    treeSet.seed = stringToInt(s.substring(0, NUMBER_LENGTH));
    int sStart = NUMBER_LENGTH;
    int sStop = 2 * NUMBER_LENGTH;
    int index = 1;
    int weightIndex = 0;
    while (index < length) {
      weights[weightIndex] = Float.intBitsToFloat(stringToInt(s.substring(sStart, sStop)));
      sStart += NUMBER_LENGTH;
      sStop += NUMBER_LENGTH;
      ++weightIndex;
      ++index;
    }
    treeSet.weights = weights;
    return treeSet;
  }

  static public ForestModel fromSeedsAndWeights(int seed, float[] weights) {
    ForestModel treeSet = new ForestModel();
    treeSet.seed = seed;
    treeSet.weights = weights;
    return treeSet;
  }

  @Override
  public float getAverageWeight() {
    float weight = 0;
    int length = weights.length;
    for (int i = 0; i < length; ++i) {
      float alpha = i / (float) length;
      float beta = 1.0f - alpha;
      weight = (alpha * weight) + (beta * weights[i]);
    }
    return weight;
  }

  @Override
  public float getWeight(int index) {
    return weights[index];
  }

  @Override
  public float[] getWeights() {
    return weights;
  }

  @Override
  public int getSeed() {
    return seed;
  }

  @Override
  public String toDisplayString() {
    StringBuilder s = new StringBuilder();
    s.append(seed).append(COMMA);
    int length = weights.length;
    for (int i = 0; i < length; ++i) {
      s.append(weights[i]).append(NEWLINE);
    }
    return s.toString();
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append(intToChars(seed));
    int length = weights.length;
    for (int i = 0; i < length; ++i) {
      s.append(intToChars(Float.floatToIntBits(weights[i])));
    }
    return s.toString();
  }

  private static char[] intToChars(int i) {
    char[] c = new char[2];
    c[0] = (char) (i & 0x0000FFFF);
    c[1] = (char) ((i >> 16) & 0x0000FFFF);
    return c;
  }

  private static int stringToInt(String s) {
    char[] c = s.toCharArray();
    if (c.length != 2) {
      throw new RuntimeException("stringToInt of String \"" +
          new String(c) + "\" of length " + c.length);
    }
    int i = 0;
    i = i | ((int) c[1]);
    i = i << 16;
    i = i | ((int) c[0]);
    return i;
  }
}
