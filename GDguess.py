# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:57:36 2017
@author: Administrator
验证哥德巴赫猜想，即对于一个大于2的偶数p，存在两个质数m，n使m+n=p成立
"""

def isprime(numb):
    if numb<2:
        return False
    elif numb == 2:
        return True
    else:
        for i in range(2, numb):
            if numb%i == 0:
                return False
    return True

while True:
    try:
        instr = raw_input('Please enter an even number: ')
        innum = int(instr)
        if innum%2 != 0 or innum<3:
            print 'Error number, try again!'
            continue
        else:
            break
    except:
        print 'Input is not a number, try again!'
        continue

for i in range(1, innum/2+1):
    if isprime(i) and isprime(innum-i):
        print '{}+{} = {}'.format(i, innum-i, innum)
