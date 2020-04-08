#!/usr/bin/python3

from z3 import *
import argparse
import itertools
import time
from subprocess import call



var_counter = 0
def count():
    global var_counter
    count = var_counter
    var_counter = var_counter +1
    return str(count)

def get_fresh_bool( suff = "" ):
    return Bool( "b_" + count() + "_" + suff )

def get_fresh_vec( vs, suff = "" ):
    n_vs = []
    for v in vs:
        n_vs.append( get_fresh_bool( suff ) )
    return n_vs

# substitutes a vector of variables
def substitute_vars( formula, from_vars, to_vars ):
    f = formula
    for j in range( 0, len(from_vars) ):
        f = substitute( f, (from_vars[j], to_vars[j]) )
    return f
#-------------------------------
# Exercise :
# consider the following state machine with three bits
#   p' = q \/ r
#   q' = ~p /\ r
#   r' = (q == p)
#
# The machine updates value of the above variables according
# to the above update function. Primed variables indicated
# the next value of the bits
#
# 
# Using SAT solver find a cycle of three states of the state machine
#   -- the cycle must have 3 distinct states
#   -- the states may occur in any order
#----------------------------------


# state machine 

p = Bool("p")
q = Bool("q")
r = Bool("r")

p_update = Or( q, r )
q_update = And( Not(p), r )
r_update = Not( q == p )

vs  = [p       ,q       ,r       ]
ups = [p_update,q_update,r_update]

tmp1 = p
tmp2 = q
tmp3 = r

while True:
    
    s1p = substitute_vars(tmp1, vs, ups)
    s1q = substitute_vars(tmp2, vs, ups)
    s1r = substitute_vars(tmp3, vs, ups)

    s2p = substitute_vars(s1p, vs, ups)
    s2q = substitute_vars(s1q, vs, ups)
    s2r = substitute_vars(s1r, vs, ups)

    s3p = substitute_vars(s2p, vs, ups)
    s3q = substitute_vars(s2q, vs, ups)
    s3r = substitute_vars(s2r, vs, ups)

    
    n1 = Or(And(s1p,tmp1),And(Not(s1p,tmp1)))
    n2 = Or(And(s1q,tmp2),And(Not(s1q,tmp2)))
    n3 = Or(And(s1r,tmp3),And(Not(s1r,tmp3)))

    n4 = Or(And(s2p,s1p),And(Not(s2p,s1p)))
    n5 = Or(And(s2q,s1q),And(Not(s2q,s1q)))
    n6 = Or(And(s2r,s1r),And(Not(s2r,s1r)))
    
    nups = [s3p,s3q,s3r]
    Fp = Or(And(nups[0],tmp1),And(Not(nups[0],tmp1)))
    Fq = Or(And(nups[1],tmp2),And(Not(nups[1],tmp2)))
    Fr = Or(And(nups[2],tmp3),And(Not(nups[2],tmp3)))

    s = Solver()
    s.add(Fp)
    s.add(Fq)
    s.add(Fr)
    s.add(Not(And(n1,n2,n3)))
    s.add(Not(And(n1,n2,n3)))
    if (s.check()==sat):
        m = s.model()
        print(m[tmp1])
        print(m[tmp2])
        print(m[tmp3])
        break
    else:
        print("us")
    tmp1 = s1p
    tmp2 = s1q
    tmp3 = s1r
    

#----------------------------------------
# a few utitilities 


# supply for fresh bools


#-----------------------------------


