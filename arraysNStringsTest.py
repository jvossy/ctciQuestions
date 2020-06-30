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
    def test_words(self):
        s = "there"
        t = "three"
        self.assertTrue(a.checkPermutation(s,t))
    def test_more_words(self):
        s = 'read'
        t = 'bread'
        self.assertFalse(a.checkPermutation(s,t))



if __name__ == '__main__':
    unittest.main()

