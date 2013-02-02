// Copyright 2012 Colin McDonough

package com.colinmcdonough.java.cloudlearning.server;

import java.util.ArrayList;

/**
 * Class to store data.
 * TODO(cmcdonough): Make this an interface or abstract class.
 * @author Colin McDonough (cmcdonough@wustl.edu)
 *
 */
public class Dataset {
	ArrayList<Entry> entries;
    int[] mins;
    int[] maxes;

	public Dataset() {
		entries = new ArrayList<Entry>();
	}

	public Dataset(int numEntries) {
		entries = new ArrayList<Entry>(numEntries);
	}

	public void addEntry(String id, String clazz, int[] attributes) {
		entries.add(new Entry(id, clazz, attributes));
	}
	
	public void setRanges(int[] mins, int[] maxes) {
	  this.mins = mins;
	  this.maxes = maxes;
	}
	
	public float getMin(int attribute) {
	  //return 0.0f;
	  return mins[attribute];
	}
	
	public float getMax(int attribute) {
	  //return 1.0f;
	  return maxes[attribute];
	}
	
	public int getEntryAttribute(int entry, int attribute) {
		return entries.get(entry).attributes[attribute];
	}
	
	public int[] getEntryAttributes(int entry) {
	  return entries.get(entry).attributes;
	}
	
	public String getClazz(int index) {
		return entries.get(index).clazz;
	}

	public int getNumAttributes() {
		if (entries.size() == 0) {
			return 0;
		}
		return entries.get(0).attributes.length;
	}

	public int getNumEntries() {
		return entries.size();
	}

	@Override
	public String toString() {
		String s = "";
		for (Entry entry : entries) {
			s += entry.toString() + "\n";
		}
		return s;
	}

	private static class Entry {
		final private String id;
		final private String clazz;
		final private int[] attributes;
		private Entry(String id, String clazz, int[] attributes) {
			this.id = id;
			this.clazz = clazz;
			this.attributes = attributes;
		}

		@Override
		public String toString() {
			String s = "";
			for (int i : attributes) {
				s += i + ", ";
			}
			return id + ", " + clazz + ", " + s;
		}
	}
}
