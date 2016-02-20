# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:52:38 2016

@author: RYAN
"""

import sys

def hello(a, b):
    print "hello and that's your sum:"
    sum=a+b
    print sum

print "hello"
print str(sys.argv)
print "world"

hello(int(sys.argv[1]), int(sys.argv[2]))

f = open("C:\Users\RYAN\Documents\GitHub\Realtime_Simulator\Python\hello.txt", "w")
f.write("hello world! \n")
f.close()