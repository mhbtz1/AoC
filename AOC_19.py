from collections import defaultdict

class ID:
    def __init__(self, num, str):
        self.num = num
        self.str = str

inp = [ (i.split('\n'))[0] for i in open("AOC_19.txt").readlines()]
idx = inp.index('split')
inp_2 = inp[idx+1:]
inp = inp[0:idx]
print(inp)
print(inp_2)
#inp = inp[0:inp.find("split")]
#inp2 = inp[inp.find("split"):]
inp = [i.split('|') for i in inp]
sub_array= []
not_processed = []#stores keys that are yet to be processed (initially those that are not just a character)
adj_list = defaultdict(list)#creates an adjacency list structure for the input
pot_strings = defaultdict(list) #stores potential strings that can be formed from a combination of given rules
def if_solve(case):
    for elem in case:
        if(elem in not_processed):
            return False
    return True
def solve_it(I_D,case):
    pos_strings = []
    ret_arr = []
    for elem in case:
        tmp_arr = pot_strings[elem]
        pos_strings.append(tmp_arr)
    #print(pos_strings)
    #max number of dependencies seems to be 3
    if(len(pos_strings)==3):
        for j in pos_strings[0]:
            for k in pos_strings[1]:
                for l in pos_strings[2]:
                    if( str(j)+str(k)+str(l) not in pot_strings[I_D]):
                        pot_strings[I_D].append(j+k+l)
    elif(len(pos_strings)==2):
        print(I_D)
        print(pos_strings[0])
        print(pos_strings[1])
        for j in pos_strings[0]:
            for k in pos_strings[1]:
                print("TWO DEPENDENCIES: " + str(j) + " " + str(k) )
                if( (j+k) not in pot_strings[I_D]):
                    pot_strings[I_D].append( (j+k) )
    elif(len(pos_strings)==1):
        for e in pos_strings:
            pot_strings[I_D].append(e)
def is_number(string):
    for char in string:
        if(not char.isdigit() ):
            return False
    return True  
def parse_input():
    for j in inp:
        k = j[0]
        tmp_k = k
        sub = k[k.find(':')+1:]
        enter = []
        cur_idx = 0
        sub=sub.split()
        print(sub)
        for elem in sub:
            if( not is_number(elem) ):
                continue
            enter.append( int(elem) )
        if(len(enter)>0):
            adj_list[int(tmp_k[0:tmp_k.find(':')])].append(enter)
        if(len(adj_list[int(tmp_k[0:tmp_k.find(':')])])==0 ):
            if(int(tmp_k[0:tmp_k.find(':')])==97):
                pot_strings[int(tmp_k[0:tmp_k.find(':')])].append(tmp_k[5])
            else:
                pot_strings[int(tmp_k[0:tmp_k.find(':')])].append(tmp_k[4])
            s = int(tmp_k[0:tmp_k.find(':')])
            sub_array.append(s)
        if(len(j)==1):
            continue
        else:
            for idx in range(1,len(j)):
                enter2 = []
                cur_idx = 0
                j[idx] = j[idx].split()
                for elem in j[idx]:
                    if(not is_number(elem) ):
                        continue
                    enter2.append( int(elem) )
                adj_list[int(j[0][0:j[0].find(':')])].append(enter2)
def solve_part_one():
    for a,b in adj_list.items():
        if(a not in sub_array):
            not_processed.append(a)
        else:
            print("VALID: " + str(a))
    #print(not_processed)
    
    while(len(not_processed)>0):
        print(pot_strings.items())
        print('__________________________________')
        removal = []
        for j in range(len(not_processed)):
            amt = 0
            ls = adj_list[not_processed[j]]
            for lis in ls:
                if(if_solve(lis)):
                    solve_it(not_processed[j], lis)
                    amt += 1
            if(amt == len(adj_list[not_processed[j]])):
                removal.append(not_processed[j])
        for r in removal:
            not_processed.remove(r)
    
parse_input()

#print(adj_list.items())
solve_part_one()

set_strings = pot_strings[0]
print(set_strings)
ans = 0
for s in set_strings:
    if(s in inp_2):
        ans += 1
print(ans)


                




