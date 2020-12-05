import os
import sys
import numpy
import random
import math

inp = [a for a in open("AOC_5.txt").readlines()]

l_x = 0
r_x = 127
col_l_x=0
col_r_x=7



def narrow(op):
    for i in range(len(op)):
        global l_x,r_x,col_l_x,col_r_x
        print("{},{},{},{}".format(l_x,r_x,col_l_x,col_r_x))
        if(op[i]=='F'):
            r_x = round((r_x+l_x+1)/2 - 1)
        elif(op[i]=='B'):
            l_x = round((r_x+l_x+1)/2  )
        elif(op[i]=='L'):
            col_r_x=round((col_r_x+col_l_x+1)/2 - 1)
        elif(op[i]=='R'):
            col_l_x=round((col_r_x+col_l_x+1)/2 )

ans = 0
ids = []
for parsed in inp:
    narrow(parsed)
    print("{},{},{},{}".format(l_x,r_x,col_l_x,col_r_x))
    ids.append(r_x * 8 + col_r_x)
    ans = max(ans, r_x * 8 +  col_r_x)
    l_x=0
    r_x=127
    col_l_x=0
    col_r_x=7


not_exist = []
for i in range(1024):
    if( i not in ids):
        not_exist.append(i)
print(ans)
print(not_exist)
    




