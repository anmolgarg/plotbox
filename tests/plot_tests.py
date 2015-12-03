'''
nose test suite for stencil module

To run some specific tests below use;
nosetests -w tests tests/stencil_tests.py:test_series_loader
'''



from nose.tools import *
import relpy as rp

import datetime
import pandas as pd



def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "Test basic"

