#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:36:35 2017

@author: lihu
"""

import re
import xlwt

outwb = xlwt.Workbook(encoding='utf-8')
outsheet = outwb.add_sheet('sheet1')

with open('./014.txt', 'r') as f:
    tex = f.readlines()
    for row in range(len(tex)):
        var = re.findall(r'.*(\d+).*"(.*)".(\d+).(\d+).(\d+).*', tex[row])
        if var:
            for col in range(len(var[0])):
                outsheet.write(row, col, var[0][col])

outwb.save('./014.xls')
