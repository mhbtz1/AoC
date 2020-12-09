from sortedcontainers import SortedList, SortedSet, SortedDict
from bisect import bisect_left
import math
import itertools

WINDOW_SIZE = 25
nums = [a.split('\n') for a in open("AOC_9.txt","r")]
psums = [0 for i in range(len(nums))]
print(nums)
for i in range(len(nums)):
    if(len(nums[i])>1):
        ls = nums[i][0:len(nums[i])-1]
        nums[i] = int(ls[0])
    else:
        nums[i] = int(str(nums[i][0]))
tmp = [nums[i] for i in range(WINDOW_SIZE)]

def remap():
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
    return tmp
tmp = remap()
#solved by applying 2SUM on some automatically balancing structure (i chose to use set), but I am fairly certain that a more optimal solution may exist, 
#and if not it certainly does for certain specific test cases(reminds me of 3SUM problem from USACO Gold)
def exists(vl,idx):
    l = 0
    r = WINDOW_SIZE-1
    tmp_s = SortedSet(nums[idx:WINDOW_SIZE+idx])
    while(l < r):
        #print(l,r)
        wt = tmp_s[l] + tmp_s[r]
        if(wt > vl):
            r -= 1
        elif(wt < vl):
            l += 1
        else:
            return True
    return False

def solve_p1():
    for idx in range(WINDOW_SIZE, len(nums)):
        if(not exists(nums[idx],idx-WINDOW_SIZE)):
            return nums[idx]
    return -1
cache = solve_p1()

#this can be done in O(N lg N) time by observing that the prefix sum function is monotonic, 
#and using sparse table/segtree for RMQ(for convenience, ill just do linear search).


#Overall optimal complexity should be O(N lg N), with an O(N lg N) precomputation for the sparse table or segment tree data structure

def min_interval(l,r):
    ans = 1000000000000000
    for i in range(l,r+1):
        ans = min(ans,nums[i])
    return ans
def max_interval(l,r):
    ans = 0
    for i in range(l,r+1):
        ans = max(ans,nums[i])
    return ans
def solve_p2():
    psums[0] = nums[0]
    for i in range(1,len(nums)):
        psums[i] = psums[i-1] + nums[i]
    #print(psums)
    tot_mn = 100000000000000
    tot_mx = 0
    cached_pot = []
    for i in range(0,len(psums)):
        l = i
        r = len(nums)-1
        #print("INDEX: " + str(i))
        mn = 1000000000000000
        mx = 0
        while(l < r):
            md = int( float(l) + round(float(r-l)/float(2)) + 1 ) 
            VAL = psums[md] - (0 if l -1 < 0 else psums[l-1])
            #print(VAL)
            #print(l,r,psums[md+1]-psums[max(l-1,0)])
            if(VAL > cache):
                r = md-1
            elif(VAL < cache):
                l = md
            else:
                #print("FOUND!")
                mn1 = min_interval(l,r)
                mx1 = max_interval(l,r)
                #print(mn1,mx1)
                mn = min(mn1,mn)
                mx = max(mx1,mx)
                r= md-1
                cached_pot.append(nums[l:md+1])
        tot_mn = min(tot_mn,mn)
        tot_mx = max(tot_mx,mx)
    return tot_mn + tot_mx

print("PART 1: " + str(cache))
print("PART 2: " + str(solve_p2()))
    
