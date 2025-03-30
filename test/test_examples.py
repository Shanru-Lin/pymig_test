#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for example module."""

import pytest
import sys
try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

from example import ExampleClass, divide

class TestExampleClass(object):
    def setup_method(self):
        self.example = ExampleClass("test_instance")
    
    def test_initialization(self, monkeypatch):
        # Capture stdout to verify print statements
        captured_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', captured_output)
        
        example = ExampleClass("new_test")
        assert "Initialized with: new_test" in captured_output.getvalue()
        assert example.name == "new_test"
    
    def test_process_items(self, monkeypatch):
        captured_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', captured_output)
        
        items = {"key1": "value1", "key2": "value2"}
        list(self.example.process_items(items))  # Consume generator
        
        output = captured_output.getvalue()
        assert "key1: value1" in output
        assert "key2: value2" in output

def test_divide():
    # Test Python 2 integer division
    assert divide(5, 2) == 2
    assert divide(10, 3) == 3
    
    # Test with floats
    assert divide(5.0, 2) == 2.5
