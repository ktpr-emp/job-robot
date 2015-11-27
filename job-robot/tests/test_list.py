#!/usr/bin/python2.6                                                                                         
# -*- coding: utf-8 -*-                                                                                      

from nose.tools import *

class TestList(object):                                                                                 
    def test_list(self):                                                                                     
        numbers = xrange(10)                                                                                 
        eq_(len(numbers), 10)                                                                                
        assert max(numbers) == 9                                                                             
        assert_equal(sum(numbers), 111)                                                                       

def test_list():                                                                                             
    numbers = xrange(10)                                                                                     
    assert_equal(len(numbers), 10)                                                                           
    assert_equal(max(numbers), 1)                                                                            
    assert_equal(sum(numbers), 2)
