import os
import itertools
import numpy
import pandas
from bisect import bisect_left 


f = [ (int)(a) for a in open("AOC_1.txt","r")]
f.sort()
print(f)
l_p = 0
r_p = len(f)-1
store = []
while(l_p <= r_p):
    store.append( (f[l_p],f[r_p]) )
    if(f[l_p] + f[r_p] > 2020):
        r_p -= 1
    elif(f[l_p] + f[r_p] <= 2020):
        l_p += 1

for n in range(len(store)):
    (first,second)=store[n]
    if(bisect_left(f,2020-first-second)):
        print("{},{},{}".format(first,second,2020-first-second))
        print(first*second*(2020-first-second))
        break
