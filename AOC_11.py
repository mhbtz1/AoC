import copy

a = [i[0:len(i)] for i in open("AOC_11.txt","r")]
print(len(a))
for i in range(len(a)):
    a[i] = list(a[i])
    if(i != len(a)):
        a[i] = a[i][0:len(a)-1]#some weird stuff occuring with new lines causes this to be iffy sometimes
for ls in a:
    print(ls)
dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,-1,1,1,-1]
ITERATIONS = 37
SZ_X = 91  #91
SZ_Y = 90 #90

#the idea is that since the boolean function of seeing a seat or not at some point is FALSE FALSE FALSE FALSE .... TRUE TRUE TRUE TRUE, the point at which FALSE -> TRUE can be binsearched for efficiently
#this should give a runtime comparable to part 1, although a bit slower due to logarithms; note this is a binsearch on distance, not point
#never mind I decided to write a godforsaken linear search

def bsearch_tot(x,y):
    const_x=x
    const_y=y
    pot = []
    const_x += 1
    #print("FIRST")
    while(const_x < SZ_X and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#')): 
        if(const_x >= SZ_X or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x += 1
    const_x = x
    const_x -= 1
    #print("SECOND")
    while(const_x >= 0 and(a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):
        if(const_x < 0 or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x -= 1
    const_x=x
    const_y += 1
    #print("THREE")
    while(const_y < SZ_Y and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):
        if(const_y >= SZ_Y or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_y += 1
    const_y=y
    const_y -= 1
    #print("FOUR")
    while(const_y >= 0 and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):         
        if(const_y < 0 or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_y -= 1
    const_y=y
    const_x+=1
    const_y-=1
    #print("FIVE")
    while(const_x < SZ_X and const_y >= 0 and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):         
        if(const_x >= SZ_X or const_y < 0 or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x+=1
        const_y-=1
    const_x=x
    const_y=y
    const_x-=1
    const_y+=1
    #print("SIX")
    while(const_x >= 0 and const_y < SZ_Y and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):         
        if(const_x <= 0 or const_y >= SZ_Y or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x-=1
        const_y+=1
    const_x=x
    const_y=y
    const_x-=1
    const_y-=1
    #print("SEVEN")
    while(const_x >= 0 and const_y >= 0 and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):
        if(const_x < 0 or const_y < 0 or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x-=1
        const_y-=1
    const_x=x
    const_y=y
    const_x+=1
    const_y+=1
    #print("EIGHT")
    while(const_x < SZ_X and const_y < SZ_Y and (a[const_x][const_y] =='.' or a[const_x][const_y]=='#') ):         
        if(const_x >= SZ_X or const_y >= SZ_Y or a[const_x][const_y]=='#'):
            pot.append( (const_x,const_y) )
            break
        const_x+=1
        const_y+=1
    ANS = 0
    print(pot)
    for pt in pot:
        x,y = pt
        if(x<0 or y<0 or x>= SZ_X or y >= SZ_Y or a[x][y] != '#'):
            continue
        ANS += 1
    return ANS
    


def second_num_adj():
    res_mat = [ [0 for i in range(SZ_Y)] for j in range(SZ_X) ]
    for i in range(SZ_X):
        for j in range(SZ_Y):
            if(a[i][j] == '.'):
                continue
            res_mat[i][j] = bsearch_tot(i,j)
    print(res_mat)
    return res_mat







def num_adj():
    ans = 0
    res_mat = [ [0 for i in range(SZ_Y)] for j in range(SZ_X) ]
    #print("START")
    for i in range(SZ_X):
        for j in range(SZ_Y):
            for k in range(len(dx)):
                if(i+dx[k] >= SZ_X or i + dx[k] < 0):
                    continue
                if(j + dy[k] >= SZ_Y or j + dy[k] < 0):
                    continue
                if(a[i + dx[k]][j + dy[k]] =='#'):
                    res_mat[i][j] += 1
    return res_mat

def step_automata(a):
    use = num_adj()
    print('\n')
    print('\n')
    for i in range(SZ_X):
        for j in range(SZ_Y):
            if(a[i][j] == '#' and use[i][j] >= 4):
                a[i][j] = 'L'
            elif(a[i][j] == 'L' and use[i][j] == 0):
                a[i][j] = '#'
            

    return a
def step_automata_two(a):
    use = second_num_adj()
    print('\n')
    print('\n')
    for i in range(SZ_X):
        for j in range(SZ_Y):
           # print(i,j,a[i][j])
            if(a[i][j] == '#' and use[i][j] >= 5):
                a[i][j] = 'L'
            elif(a[i][j] == 'L' and use[i][j] == 0):
                a[i][j] = '#'
    return a


def solve_p1():
    while(True):
        global a
        tmp = copy.deepcopy(a)
        a=step_automata(a)
        for ls in a:
            print(ls)
        if(tmp == a):
                break

    ANS = 0
    for i in range(SZ_X):
        for j in range(SZ_Y):
            if(a[i][j]=='#'):
                ANS += 1
    return ANS

#second_num_adj()
def solve_p2():
    while(True):
        global a
        tmp = copy.deepcopy(a)
        a=step_automata_two(a)
        #for ls in a:
            #print(ls)
        if(tmp == a):
             break
    ANS = 0
    for i in range(SZ_X):
        for j in range(SZ_Y):
            if(a[i][j]=='#'):
                ANS += 1
    return ANS






#print("PART 1: " + str(solve_p1()) )

print("PART 2: " + str(solve_p2()) )

