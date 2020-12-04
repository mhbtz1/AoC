from collections import defaultdict 
sz = len(inp)
se = set()
de = {}
print(inp);
hcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def l_to_s(l):
    r=''
    for i in range(len(l)-1):
        r += l[i]
        r += ','
    r += l[len(l)-1]
    print(r)
    return r
f = open("AOC_4.txt","r")
inp = [a.split() for a in f]
for i in range(len(inp)):
    if(len(inp[i])==0):
        continue
    inp[i]=l_to_s(inp[i])
    inp[i] = inp[i].split(',')


def chk_ascii(j):
    for i in range(len(j)):
        if(ord(j[i])>102):
            return False
    return True

def chk():
    ans = True
    global de
    for (i,j) in de.items():
        print("FORM: {}, {}".format(i,j))
        print('\n')
        if(i=="byr"):
                vl = int(j)
                if(not (vl >= 1920 and vl <= 2002) ):
                    ans=False
                    break
        elif(i=="iyr"):
                vl = int(j)
                if(not (vl >= 2010 and vl <= 2020) ):
                    ans=False
                    break
        elif(i=="eyr"):
                vl = int(j)
                if( not (vl >= 2020 and vl <= 2030) ):
                    ans = False
                    break
        elif(i=="hgt"):
                vl = int(j[0:len(j)-2])
                if(j[len(j)-2:]=="cm"):
                    if( not( vl >= 150 and vl <= 193) ):
                        ans = False
                        break
                else:
                    if( not (vl >= 59 and vl <= 76) ):
                        ans = False
                        break
        elif(i=="hcl"):
                ret = j[0]=='#' and chk_ascii(j)
                if( not ret):
                    ans = False
                    break
        elif(i=="ecl"):
                if(not (j in hcl) ):
                    ans = False
                    break
        elif(i=="pid"):
                print(len(j))
                if(len(j) != 9):
                    ans = False
                    break
    return ans

ans = 0
for j in range(len(inp)):
    if(len(inp[j])==0):#signifies a new line sign
        if(len(se)==8 or (len(se)==7 and "cid" not in se) ):
            res = chk()
            if(res):
                ans += 1
        de.clear()
        se.clear()
    for k in range(len(inp[j])):
        tmp = inp[j][k]
        tmp_sub = tmp[0:inp[j][k].find(":")]
        tmp_two = tmp[inp[j][k].find(":")+1:]
        se.add(tmp_sub)
        de[tmp_sub]=(tmp_two)
print(ans)

