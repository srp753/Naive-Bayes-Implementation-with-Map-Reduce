#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:03:03 2017

@author: snigdha
"""

import sys
import re
def tokenizeDoc(cur_doc):
    return re.findall('\\w+',cur_doc)


for line in sys.stdin:
    entry = line.split("\t")
    a = tokenizeDoc(entry[1])
    for label in a:
        print("Y="+ label)
        print("Y=*")
        b = tokenizeDoc(entry[2])
        for word in b:
            print("Y="+label+","+"W=*")
            print("Y="+label+","+"W="+word)
        
