from collections import defaultdict
dic = defaultdict(list)
vis = {}
st = set()
table = {}
#Part 1 is reversing the direction of the edges from the bags and dfs'ing from the gold bag, and finding component sizes
#Part 2 is dp on a dag: let dp[i] be the amount of nested bags in the subtree with root i, dp[i] = 1 + (dp[j]*amt[j]) for j which are the children of i


class Bag:
    def __init__(self, amt, i_d):
        self.amt=amt
        self.i_d=i_d
def f_num(s):
    for i,c in enumerate(s):
        if(c.isdigit()):
            return i
    return -1

def dfs1(node):
    g = dic[node]
    if(node not in vis):
        print(node)
        vis[node] = True
        if( not (node=='shiny gold bag' or node =='shiny gold bags') ):
            st.add(node)
        for bg in g:
          #if(bg.i_d != "shiny gold bag" and bg.i_d != "shiny gold bags"):
          dfs(bg.i_d)
          dfs(bg.i_d + 's')
def dfs2(node,tmp):
    g = dic[node.i_d]
    tmp1 = node.i_d
    if(tmp1[len(tmp1)-1] != 's'):
        tmp1 += 's'
    table[tmp1] = 1
    print(tmp1)
    for bg in g:
        addS = bg.i_d
        if(addS[len(addS)-1] != 's'):
            addS += 's'
        if(addS != tmp1):
            dfs2(Bag(bg.amt,addS), Bag(node.amt,tmp1))
        print("BACKTRACK: " + str(tmp1) + " " + str(addS))
        table[tmp1] += (bg.amt) * (table[addS])


i_ = [a for a in open("AOC_7.txt").readlines()]
i_ = str(i_)
i_ = i_.split('\\n')

for idx in range(len(i_)):
    j = i_[idx]
    tmp = j.find("bags")
    if(idx==0):
        s_str = j[2:tmp+5]
    else:
        s_str = j[4:tmp+4]
    t_str = j[tmp+5:].split(',')
    for k in t_str:
        vl = f_num(k)
        if(vl==-1):
            continue
        else:
            s = k[vl+1:len(k)]
            if(s[0]==' '):
                s=k[vl+2:len(k)]
            if(s[len(s)-1]=='.'):
                s=s[0:len(s)-1]
            #print("AMT: " + str(int(k[vl])))
            #print("BAG: " + str(s))
            s_str = s_str.strip()
            s = s.strip()
            print(str(s_str) + str(s))
            #DICTIONARY FOR PART 1:
            #dic[s].append(Bag(int(k[vl]),s_str))
            #DICTIONARY FOR PART 2:
            dic[s_str].append(Bag(int(k[vl]),s))
            #print(s)


#PART 1
'''
lst = dic['shiny gold bags']
dfs('shiny gold bag')
print('\n')
dfs('shiny gold bags')
print('\n')
print(len(st)/2)
'''
#PART 2
tmp1 = Bag(1,'')
dfs2(Bag(1,'shiny gold bags'),tmp1)
#dfs2(Bag(1,'shiny gold bag'),tmp1)
#print('\n')
#dfs2(Bag(1,'shiny gold bags'),tmp1)
print('\n')
ans = table['shiny gold bags']
#ans2 = table['shiny gold bag']
    
print(ans-1)
#print(ans2)
