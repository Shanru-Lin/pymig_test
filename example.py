#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example module with Python 2 code that needs migration."""

from __future__ import print_function
import sys
import urllib2  # Python 2 specific import

class ExampleClass(object):  # Python 2 style class definition
    def __init__(self, name):
        self.name = name
        print "Initialized with:", name  # Python 2 print statement
    
    def fetch_data(self, url):
        """Fetch data from URL using Python 2 urllib2."""
        try:
            response = urllib2.urlopen(url)
            return response.read()
        except urllib2.URLError, e:  # Python 2 exception syntax
            print "Error fetching URL:", e
            return None
    
    def process_items(self, items):
        """Process items using Python 2 idioms."""
        # Python 2 dict.iteritems()
        for key, value in items.iteritems():
            print "%s: %s" % (key, value)  # Old string formatting
        
        # Python 2 range vs xrange
        for i in xrange(5):
            yield i

# Python 2 style integer division
def divide(a, b):
    return a / b  # In Python 2, returns integer result for integer inputs

# Python 2 input vs raw_input
def get_user_input():
    return raw_input("Enter something: ")

if __name__ == "__main__":
    print "Running example.py"  # Python 2 print
    example = ExampleClass("test")
    items = {"a": 1, "b": 2, "c": 3}
    example.process_items(items)
    print "5/2 =", divide(5, 2)  # Will print "5/2 = 2" in Python 2
