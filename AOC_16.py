#pretty shitty problem honestly

class Pair:
    def __init__(self,f,s):
        self.f=f
        self.s=s
         

a = [ (a.split('\n'))[0] for a in open("AOC_16.txt").readlines()]
vals = []
candidates = []

print(a)
def parse_input():
    idx = 0
    global a
    for interval in a:
        idx += 1
        print(interval)
        if(len(interval)==0):
            break
        interval = interval.split()
        print(interval)
        one = interval[1]
        left_one, right_one = int(one[0:one.find('-')]), int(one[one.find('-')+1:])
        two = interval[3]
        left_two, right_two = int(two[0:two.find('-')]), int(two[two.find('-')+1:])
        print(left_one,right_one,left_two,right_two)
        vals.append(Pair(left_one,right_one))
        vals.append(Pair(left_two,right_two))
    t = a[idx+1].split(',')
    t = [int(i) for i in t]
    idx += 4

    for ptr in range(idx,len(a)):
        tmp = a[ptr].split(',')
        tmp = [int(j) for j in tmp]
        for j in tmp:
            candidates.append(j)

    ans = 0
    print(candidates)
    for j in candidates:
        res = False
        for k in vals:
            if( k.f <= j and j <= k.s):
                res=True
                break
        if(not res):
            print("INVALID: " + str(j))
            ans += j

    print(ans)
parse_input()
