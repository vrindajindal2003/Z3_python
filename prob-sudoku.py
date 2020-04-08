
#!/usr/bin/python3

from z3 import *
import argparse
import itertools
import time

problem1 = [
 [ 9, 0, 0,   0, 1, 0,   5, 0, 0],
 [ 7, 0, 0,   8, 0, 3,   0, 0, 2],
 [ 0, 0, 0,   0, 0, 0,   3, 0, 8],

 [ 0, 7, 8,   0, 2, 5,   6, 0, 0],
 [ 0, 0, 0,   0, 0, 0,   0, 0, 0],
 [ 0, 0, 2,   3, 4, 0,   1, 8, 0],

 [ 8, 0, 9,   0, 0, 0,   0, 0, 0],
 [ 5, 0, 0,   4, 0, 1,   0, 0, 9],
 [ 0, 0, 1,   0, 5, 0,   0, 0, 4]
]

problem2 = [
[ 0, 8, 0,   0, 0, 3,   0, 0, 0],
[ 5, 0, 3,   0, 4, 0,   2, 0, 0],
[ 7, 0, 4,   0, 8, 0,   0, 0, 3],

[ 0, 7, 0,   0, 0, 0,   5, 0, 0],
[ 0, 3, 0,   8, 0, 5,   0, 6, 0],
[ 0, 0, 1,   0, 0, 0,   0, 9, 0],

[ 9, 0, 0,   0, 3, 0,   7, 0, 6],
[ 0, 0, 7,   0, 2, 0,   3, 0, 1],
[ 0, 0, 0,   6, 0, 0,   0, 2, 0]
]

problem3 = [
[ 7, 0, 0,   8, 0, 5,   0, 0, 6],
[ 0, 0, 4,   0, 6, 0,   2, 0, 0],
[ 0, 5, 0,   2, 0, 4,   0, 9, 0],

[ 8, 0, 5,   0, 0, 0,   3, 0, 9],
[ 0, 1, 0,   0, 0, 0,   0, 6, 0],
[ 3, 0, 6,   0, 0, 0,   1, 0, 7],

[ 0, 6, 0,   5, 0, 7,   0, 1, 0],
[ 0, 0, 7,   0, 9, 0,   6, 0, 0],
[ 5, 0, 0,   3, 0, 6,   0, 0, 2]
]

problem = problem1
# problem = problem2

# define the problem variables
# Hint: three dimentional array

arr=[[[Bool('p'+str(i)+str(j)+str(k)) for k in range(1,10)] for j in range(1,10)] for i in range(1,10)]





def sum_to_one( ls ):
    phi1=Or(ls)
    l=[Or(Not(p),Not(q)) for i,p in enumerate(ls) for j,q in enumerate(ls) if i !=j]
    phi2=And(l)
    phi3=And(phi1,phi2)
    return phi3
# def sum_to_one( ls ):
    # reuse some to one code

# Accumulate constraints in the following list 

Fs1 = [sum_to_one(arr[i][j]) for i in range(9) for j in range(9)]

Fs2=[]
for j in range(9):
    for k in range(9):
        l=[]
        for i in range(9):
            l=l+[arr[i][j][k]]
        Fs2=Fs2+[sum_to_one(l)]
Fs3=[]
for i in range(9):
    for k in range(9):
        l=[]
        for j in range(9):
            l=l+[arr[i][j][k]]
        Fs3=Fs3+[sum_to_one(l)]

Fs4=[]
for i in range(0,3):
    for j in range(0,3):
        for k in range(9):
            l=[]
            for r in range(0,3):
                for s in range(0,3):
                    l=l+[arr[3*i+r][3*j+s][k]]
            Fs4=Fs4+[sum_to_one(l)]
Fs=Fs1+Fs2+Fs3+Fs4

Fs5=[]
for i in range(9):
    for j in range(9):
        if not(problem[i][j]==0):
            # p=Bool("p")
            # p=True
            Fs5=[arr[i][j][problem[i][j]-1]]+Fs5
Fs=Fs+Fs5


# Encode already filled positions


# Encode for i,j  \sum_k x_i_j_k = 1

# Encode for j,k  \sum_i x_i_j_k = 1

# Encode for i,k  \sum_j x_i_j_k = 1

# Encode for i,j,k  \sum_r_s x_3i+r_3j+s_k = 1



s = Solver()
s.add( And( Fs ) )

if s.check() == sat:
    m = s.model()
    for i in range(9):
        if i % 3 == 0 :
            print("|-------|-------|-------|")
        for j in range(9):
            if j % 3 == 0 :
                print ("|", end =" ")
            for k in range(9):
                # FILL THE GAP
                # val model for the variables
                val = m[arr[i][j][k]]
                if is_true( val ):
                    print("{}".format(k+1), end =" ")
        print("|")
    print("|-------|-------|-------|")
else:
    print("sudoku is unsat")

# print vars
