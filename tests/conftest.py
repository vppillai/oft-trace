"""Pytest configuration file."""
import os
import sys
import pytest

# Add parent directory to path to allow importing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))