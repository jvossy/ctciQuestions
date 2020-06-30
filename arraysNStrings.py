# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:58:24 2020

@author: Vosburgh
"""

def isUnique(inStr):
    if type(inStr) != type('yoyo'):
        raise TypeError('inStr must be of type String.')
    ind = 1
    for char in inStr:
        for prior in (inStr[0:ind-1]):
            if prior == char:
                return False
        ind = ind+1
    return True

def checkPermutation(st1, st2):
    if len(st1) != len(st2):
        return False
    
    return True