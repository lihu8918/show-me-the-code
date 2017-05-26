#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:01:35 2017

@author: lihu
"""

with open('./text.txt', 'r') as f:
    sens = [line.strip() for line in f]
    user_input = raw_input(u' Please enter your words: ')
    for sen in sens:
        if sen in user_input:
            print_input = user_input.replace(sen, '*'*len(sen.decode('utf-8')))
            print print_input
            break
        else:
            continue
