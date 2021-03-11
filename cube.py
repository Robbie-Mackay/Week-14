# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:29:26 2021

@author: robbi
"""

def cube(x):
    """Returns the cube of x"""
    return x**3  # <--- This obviously doesn't work correctly

def test_square():
    assert cube(0) == 0
    assert cube(2) == 8
    assert cube(-2) == -8