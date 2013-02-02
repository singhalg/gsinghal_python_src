#!/usr/bin/perl -w
 
 use strict;
 
 while (<STDIN>) {
     chomp;
     my $Q = ord($_) - 64;
     print "Qual: $Q\n";
 }
