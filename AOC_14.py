import os
from collections import defaultdict

class Bitmask:
    def __init__(self, index, value):
        self.index = index
        self.value = value

b = defaultdict(list)
def parse_input():
    tmp_one = [i.split('\n') for i in open("AOC_14.txt").readlines()]
    a = [j[0] for j in tmp_one]
    print(a)
    cur_mask = ''
    for parse in a:
        if('[' not in parse):
            cur_mask = parse[parse.find('=')+2:]
            continue
        else:
            tmp = int(parse[parse.find('[')+1:parse.find(']')])
            val = int( parse[parse.find('=')+1:] )
            print(tmp,val)
            b[cur_mask].append(Bitmask(tmp,val))

address = [0 for i in range(10000000)]

def sim_mask():
    ans = 0
    for one,two in b.items():
        one = [c for c in one]
        #print(one)
        for j in two:
            conv =  bin(j.value)[2:]
            tmp = len(conv)
            conv = ('0' * (36-tmp) )  + conv
            conv = [c for c in conv]
            for k in range(len(one)):
                if(one[k]=='X'):
                    continue
                conv[k] = one[k]
            conv = ''.join(conv)
            print( (int(conv,2)) )
            address[j.index] = (int(conv,2))
parse_input()
sim_mask()
ans= 0
for j in address:
    if(j==0):
        continue
    ans += j
    print("ANS: " + str(ans))
print(ans)
