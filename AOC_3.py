import os
import sys
import random
import itertools
import numpy
import pandas
from bisect import bisect_left 


sys.setrecursionlimit(10000)
g = []
f = open("AOC_3.txt", "r")
for j in f.readlines():
    if(j[len(j)-1]=='\n'):
        g.append(j[0:len(j)-1])
    else:
        g.append(j)
d_e = ["" for i in range(len(g))]
for i in range(len(d_e)):
    d_e[i]=g[i]
for i in range(len(d_e)):
    print(d_e[i])

ans = 0
br = False
slp_chk = [ (1,3), (1,1), (1,5), (1,7), (2,1)]
def step_function(CUR_X,CUR_Y, idx):
    print("{},{}".format(CUR_X,CUR_Y))
    if(CUR_X>=len(d_e)-1):
        global br
        br=True
        return (CUR_X,0)
    CUR_X+=slp_chk[idx][0]
    CUR_Y+=slp_chk[idx][1]
    
    CUR_Y %= len(d_e[0])
    print(d_e[CUR_X][CUR_Y])
    if(d_e[CUR_X][CUR_Y]=='#'):
        global ans
        ans += 1
    return CUR_X, CUR_Y

cur_x=0
cur_y=0
past_ans = []
tot_ans = 1
for i in range(len(slp_chk)):
    while(not br):
        ret = step_function(cur_x,cur_y,i)
        print("{},{}".format(ret[0],ret[1]))
        cur_x=int(ret[0])
        cur_y=int(ret[1])
        #global cur_x, cur_y, tot_ans, past_ans, ans
    br=False
    tot_ans *= ans
    past_ans.append(ans)
    ans = 0
    cur_x = 0
    cur_y = 0
print(ans)
print(tot_ans)
print(past_ans)

def main():
    if '__name__'=='__main__':
        main()
