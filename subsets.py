#!/usr/bin/python3

from z3 import *
import argparse

n=11
m=8
k=3

arr=[[Bool("p_"+str(i)+" "+str(j)) for j in range(m)] for i in range(n)]

s=Solver()

for j in range(m):
    l=[]
    for i in range(n):
        l=l+[(arr[i][j],1)]
    s.add(PbEq(l,k))

for a in range(0,m):
    for b in range(a+1,m):
        l=[]
        for i in range(n):
            l=l+[(And(arr[i][a],arr[i][b]),1)]
        s.add(PbEq(l,1))

if s.check()==sat:
    mo=s.model()
    for i in range(m):
        s=str(i)+"-- "
        for j in range(n):
            val=mo[arr[j][i]]
            if is_true(val):
                s=s+str(j)+" "
            else:
                s=s
        print(s)
else:
    print("unsat")
