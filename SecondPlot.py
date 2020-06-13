# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:13:26 2020

@author: DELL USA
"""
import math
import pylab

y_values = []
x_values = []
number = 0.0

while number < math.pi * 2:
    y_values.append(math.sin(number))
    x_values.append(number)
    number += 0.1
    
pylab.plot(x_values,y_values,'ro')
pylab.show()


