import os
import itertools
import numpy
import pandas
from bisect import bisect_left 

def count(param, ch, lb, rb):
    print(param)
    print("{},{}".format(lb,rb))
    return (param[lb]==ch and param[rb]!=ch) or (param[rb]==ch and param[lb]!=ch)

tot_ans = 0
get_inp = open("AOC_2.txt","r")
for j in get_inp.readlines():
    j=j[0:len(j)]
    j = j.split(' ')
    pt = j[0]
    lb = int(pt[0:pt.find("-")])
    rb = int(pt[pt.find("-")+1:])
    let = j[1][0]
    occ = count(j[2],let,lb-1,rb-1)
    #print(j[2])
    #print(occ)
    if(occ):
        tot_ans += 1


print(tot_ans)

