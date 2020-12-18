import math
def gcd (a, b):
    while (b):
        a %= b
        tmp_a = a
        a = b
        b = tmp_a
    return a
def lcm (a, b):
    return (a / gcd(a, b) * b)
def solve_p1():
    a = [a for a in open("AOC_13.txt","r")]
    a[0]=a[0][0:len(a[0])-1]
    a[1] = a[1][0:len(a[1])-1]
    a[1] = a[1].split(',')
    v = []
    for j in range(len(a[1])):
        if(a[1][j]=='x'):
            continue
        v.append(int(a[1][j]))
    print(v)
    MIN_AMT = 1000000000000000000000000
    MIN_ID = 0
    for id_ in v:
        amt = id_
        div = math.ceil( float(int(a[0]))/float(id_) )
        #div2 = math.floor( float(int(a[0]))/float(id_) )
        print( int(a[0]), id_*div)
        if( id_*div == int(a[0])):
            continue
        MIN_AMT = min(MIN_AMT, abs( abs(int(a[0])) - id_*div) )
        if(MIN_AMT == abs( abs(int(a[0])) - id_*div) ):
            MIN_ID = id_

    print(MIN_AMT * MIN_ID)
    print(MIN_ID)
def solve_p2():
    a = open("AOC_13.txt","r").readline()
    a=a.split(',')
    v = []
    rle = []
    prod = 1
    for j in range(len(a)):
        if(a[j]=='x'):
            continue
        v.append(int(a[j])) 
        prod *= int(a[j])
        rle.append(j) 
    print(v)
    print(rle)
solve_p2()


