# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:52:38 2016

@author: RYAN
"""


import sys

filePath = "C:\Users\RYAN\Documents\GitHub\Realtime_Simulator\Python\hello" + sys.argv[2] + ".txt"
print(filePath) # print will not work when it is called by cmd


f = open(filePath, "w")
f.write("hello world! \n" + "Here's your sum: " + sys.argv[1])
f.close()