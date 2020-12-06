from collections import defaultdict

spl = open("AOC_6.txt","r").readlines()
conv = ''
for i in spl:
    conv += i
conv=conv.split('\n')
d = {}
e = set()
ans = 0
ans2 = 0
sz_grp = 0

for idx in range(len(conv)):
    i = conv[idx]
    if(len(i) != 0 ):
        for c in i:
            e.add(c)
    elif(len(i) == 0):
        ans2 += len(e)
        e.clear()
ans2 += len(e)


for idx in range(len(conv)):
    code = conv[idx]
    #print(len(code))
    if(len(code) != 0):
        sz_grp += 1
        for ch in code:
            if(str(ch) in d):
                d[str(ch)] += 1
            else:
                d[str(ch)] = 1
    if(len(code)==0 or idx==len(conv)-1 ):
        for (j,k) in d.items():
            if(d[str(j)]==sz_grp):
                ans += 1
        d.clear()
        sz_grp = 0
        
print("PART 1: " + str(ans2))
print("PART 2: " + str(ans) )
