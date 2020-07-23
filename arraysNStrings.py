# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:58:24 2020

@author: Vosburgh
"""

def isUnique(inStr):
    #Returns if a string contains only unique characters
    if type(inStr) != type('yoyo'):
        raise TypeError('inStr must be of type String.')
    ind = 1
    for char in inStr:
        ra = range(ind-1)
        for prior in ra:
            if inStr[prior] == char:
                return False
        ind = ind+1
    return True

def checkPermutation(st1, st2):
    #Returns if two strings are permutations of each other
    if len(st1) != len(st2):
        return False
    for char in st1:
        try:
            x = st2.index(char)
        except ValueError:
            return False
        st2 = st2[0:x-1] + st2[x+1:len(st2)]
    return True

def urlIfy(inStr):
    #Returns a string replacing spaces with '%20'
    outStr = inStr.replace(' ', '%20')
    return outStr