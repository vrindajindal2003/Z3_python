#!/usr/bin/python3

from z3 import *
# from solve import *
import argparse
import itertools
import time

# number of variables
n=10

# constructed list of variables
vs = [Bool('p%s' %i) for i in range(n)]


print(vs)

# write function that encodes that exactly one variable is one
def sum_to_one( ls ):
	phi1=Or(ls)
	l=[Or(Not(p),Not(q)) for i,p in enumerate(ls) for j,q in enumerate(ls) if i !=j]
	phi2=And(l)
	phi3=And(phi1,phi2)
	return phi3

    

# call the function
F = sum_to_one( vs )
print(F)

# construct Z3 solver
s=Solver()
s.add(F)
r=s.check()

# add the formula in the solver

# check sat value

if r == sat:
	m=s.model()
	# print(m)
	for i in range(n):
		if(is_true(m[vs[i]])):
			print("p"+str(i))

    # get satisfying model

    # print only if value is true

else:
    print("unsat")
