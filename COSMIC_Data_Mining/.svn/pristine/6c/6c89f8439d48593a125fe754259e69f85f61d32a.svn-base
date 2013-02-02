// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Random;

/**
 * Class to iteratively generate trees in a forest, so that only one tree must
 * is stored in memory at a time.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public class ForestIter implements LearningIter {

  private static final int UNDEFINED = -3;

  private final Node currentRoot;
  private Random currentRandom;
  private final Random random;
  private final int numTrees;
  private int currentTree;
  private final int maxDepth;
  private final double branching;
  private final Dataset dataset;
  
  private ForestIter(int numTrees, int maxDepth, int seed,
      double branching, Dataset dataset) {
    System.out.println(
        "Forest(" + numTrees + ", " + maxDepth + ", " + branching + ")");
    this.numTrees = numTrees;
    this.currentTree = 0;
    this.maxDepth = maxDepth;
    this.branching = branching;
    this.dataset = dataset;
    this.random = new Random(seed);
    this.currentRandom = new Random(random.nextInt());
    this.currentRoot = new Node();
    buildTree();
  }

  public static ForestIter getForestIter(int numTrees, int maxDepth, int seed,
      double branching, Dataset dataset) {
    return new ForestIter(numTrees, maxDepth, seed, branching, dataset);
  }

  @Override
  public boolean hasNext() {
    return currentTree < numTrees;
  }

  @Override
  public void next() {
    if (hasNext()) {
      ++currentTree;
      currentRandom = new Random(random.nextInt());
      currentRoot.index = UNDEFINED;
    } else {
      throw new NoSuchElementException("Index " + (currentTree + 1));
    }
  }

  @Override
  public List<Integer> getFeatures() {
    List<Integer> features = new ArrayList<Integer>();
    getFeatures(currentRoot, features);
    return features;
  }

  private void getFeatures(Node node, List<Integer> list) {
    if (node.index != UNDEFINED) {
      getFeatures(node.right, list);
      list.add(node.index);
      getFeatures(node.left, list);
    }
  }

  private void buildTree() {
    nodeFromDataset(currentRoot, dataset, currentRandom);
    extendTree(currentRoot, 1);
  }

  private void extendTree(Node root, int currentDepth) {
    if (root.left == null) {
      root.left = new Node();
    }
    if (root.right == null) {
      root.right = new Node();
    }
    if (currentDepth < maxDepth && currentRandom.nextFloat() < branching) {
      // Branch the node.

      nodeFromDataset(root.left, dataset, currentRandom);
      nodeFromDataset(root.right, dataset, currentRandom);

      extendTree(root.left, currentDepth + 1);
      extendTree(root.right, currentDepth + 1);
    } else {
      if (currentRandom.nextBoolean()) {
        Node left = root.left;
        left.index = Forest.ALZHIEMERS;
        Node right = root.right;
        right.index = Forest.NOT_ALZHIEMERS;
      } else {
        Node left = root.left;
        left.index = Forest.NOT_ALZHIEMERS;
        Node right = root.right;
        right.index = Forest.ALZHIEMERS;
      }
    }
  }

  private float evaluateTree() {
    int length = dataset.getNumEntries();
    int correctCount = 0;
    for (int i = 0; i < length; ++i) {
      int[] attributes = dataset.getEntryAttributes(i);
      if (dataset.getClazz(i).equals(decide(attributes))) {
        ++correctCount;
      }
    }
    float correct = correctCount / (float) length;
    correct -= 0.5f;
    correct *= 2.0f;
    return correct;
  }

  @Override
  public String decide(int[] attributes) {
    if (currentRoot.index == UNDEFINED) {
      buildTree();
    }
    return decide(attributes, currentRoot);
  }

  private static String decide(int[] attributes, Node node) {
    if (node.getIndex() == Forest.ALZHIEMERS) {
      return Forest.CLASS_ALZHIEMERS;
    } else if (node.getIndex() == Forest.NOT_ALZHIEMERS) {
      return Forest.CLASS_NOT_ALZHIEMERS;
    }
    if (node.getValue() > attributes[node.getIndex()]) {
      return decide(attributes, node.left);
    } else {
      return decide(attributes, node.right);
    }
  }

  private static void nodeFromDataset(Node node, Dataset dataset, Random random) {
    int nextIndex = (int) (random.nextFloat() * dataset.getNumAttributes());
    float range = dataset.getMax(nextIndex) - dataset.getMin(nextIndex);
    float nextAttributeValue =
        dataset.getMin(nextIndex) + (random.nextFloat() * range);
    node.index = nextIndex;
    node.decisionValue = nextAttributeValue;
  }

  @Override
  public float[] evaluateForest(Dataset dataset) {
    float[] weights = new float[numTrees];
    for (int i = 0; i < numTrees; ++i) {
      if (i % 100 == 0) {
        System.out.println("Evaluating forest (" + i + "/" + (numTrees - 1) + ")");
      }
      weights[i] = evaluateTree();
      if (!hasNext()) {
        break;
      }
      next();
    }
    return weights;
  }

  @Override
  public int size() {
    return numTrees;
  }

  private static class Node {
    private int index;
    private float decisionValue;
    private Node left;
    private Node right;

    private Node() {
      this.index = UNDEFINED;
      this.left = null;
      this.right = null;
    }

    private int getIndex() {
      return index;
    }

    private float getValue() {
      return decisionValue;
    }
  }

}
