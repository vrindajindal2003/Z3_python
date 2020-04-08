#!/usr/bin/python

from z3 import *
import argparse
import itertools
x=Bool("x")
y=Bool("y")

f=And(Or(x,Not(x)),Or(y,Not(x)))

frequency={}

def literals(f):
    if(f.children()==[]):
        if f in frequency.keys():
            frequency[f]=frequency[f]+1
            return
            print(f,frequency(f))
        else:
            frequency[f]=1
            return
    else:
        for ch in f.children():
            literals(ch)
        return

literals(f)
for k,v in frequency.items():
    print(k,v)
            

