#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:44:44 2017
@author: lihu
"""

import re

dic = {}
punc = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'

with open('./test.txt', 'r') as fid:
    for line in fid:
        line_sub = re.sub(punc, '', line)
        tokens = line_sub.strip().split()
        for token in tokens:
            if token not in dic:
                dic[token] = 0
            dic[token] += 1

for key, var in dic.items():
    print '{0:>16s} : {1:5d}'.format(key, var)
