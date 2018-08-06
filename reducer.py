#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:06:00 2017

@author: snigdha
"""

import sys
count = 1
temp = 'NULL'

for line in sys.stdin:
    line = line.strip('\n')
    if temp is not 'NULL':
        if line == temp:
            count = count + 1
            temp = line
        if line is not temp:
            print(line+"\t"+str(count))
            count = 1
            temp = line
    else:
        temp = line

print(line+"\t"+str(count))