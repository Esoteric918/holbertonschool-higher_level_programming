#!/usr/bin/python3
"""Unittest for class Rectangle"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
from io import StringIO
import pep8


class TestRectangle(unittest.TestCase):
    """Tests for class Rectangle"""
    def test_init(self):
        """Tests for __init__"""
