# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:15:42 2020

@author: Vosburgh
"""
import arraysNStrings as a
import unittest

class TestIsUnique(unittest.TestCase):
    def test_alphabet(self):
        s = 'abcdefghijklmnopqrstuvwxyz'
        self.assertTrue(a.isUnique(s))
        
    def test_words(self):
        s = 'Hello world'
        self.assertFalse(a.isUnique(s))
        
    def test_aa(self):
        s = 'aa'
        self.assertFalse(a.isUnique(s))
        
    def test_exception(self):
        s = 5
        self.assertRaises(TypeError, a.isUnique, s)

class TestCheckPermutation(unittest.TestCase):
    def test_like(self):
        s = "there"
        t = "three"
        self.assertTrue(a.checkPermutation(s,t))
        
    def test_len(self):
        s = 'read'
        t = 'bread'
        self.assertFalse(a.checkPermutation(s,t))

    def test_unalike(self):
        s = 'dread'
        t = 'bread'
        self.assertFalse(a.checkPermutation(s,t))
        
class TesturlIfy(unittest.TestCase):
    def test_no_space(self):
        s = 'alotofwords'
        r = a.urlIfy(s)
        self.assertTrue(s == r)
        
    def test_sentance(self):
        s = 'a lot of words'
        t = 'a%20lot%20of%20words'
        r = a.urlIfy(s)
        print(r)
        self.assertTrue(r == t) 
        
if __name__ == '__main__':
    unittest.main()

