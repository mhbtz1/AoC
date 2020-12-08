

a = [i for i in open("AOC_8.txt").readlines()]
for idx in range(len(a)):
    a[idx] = a[idx].split()
print(a)

#there are two cases for end: you can jump out of bounds or you can jump backwards
#to a visited operation
def arbiter(op, amt,sign):
    if(op=='nop'):
        if(amt==len(a)):
            return True
        return False
    elif(op=='acc'):
        if(amt==len(a)):
            return True
        return False
    elif(op == 'jmp'):
        if(sign == '+'):
            if(amt==len(a)-1+amt):
                return true
            return False
        else:
            if(amt==len(a)-1-amt):
                return true
            return False

class Computer:
    def __init__(self,vis,a):
        self.vis = vis
        self.a = a
    #COMPLETE SOLUTION FOR ADVENT OF CODE PROBLEM 8
    def eval_amt(self):
        ptr = 0
        ans = 0
        while(ptr not in self.vis):
            if(ptr >= len(a)):
                break
            print(a[ptr])
            self.vis[ptr] = True
            ls = self.a[ptr]
            if(ls[0]=='nop'):
                ptr += 1
            elif(ls[0] == 'acc'):
                tmp= ls[1]
                if(tmp[0] == '-'):
                    ans -= int(tmp[1:])
                else:
                    ans += int(tmp[1:])
                ptr += 1
            elif(ls[0] == 'jmp'):
                tmp = ls[1]
                if(tmp[0]=='-'):
                    ptr -= int(tmp[1:])
                else:
                    ptr += int(tmp[1:])
        self.vis.clear()
        return ans, ptr


ps = {}
true_ans = 0

print('--------------------------------------------')
for idx in range(len(a)):
    if(a[idx][0] == 'jmp'):
        a[idx][0] = 'nop'
        cm = Computer(ps,a)
        ans, ptr = cm.eval_amt()
        print(a)
        print("{},{}".format(ans,ptr))
        print('-------------------------------------------------')
        #if(ptr == len(a)-1):
        if(arbiter(a[idx][0],ptr,a[idx][1])):
            true_ans = max(true_ans,ans)
        a[idx][0] = 'jmp'
    elif(a[idx][0] == 'nop'):
        a[idx][0] = 'jmp'
        cm = Computer(ps,a)
        ans, ptr = cm.eval_amt()
        #print(a)
        print('-------------------------------------------------')
        #if(ptr == len(a)-1):
        if(arbiter(a[idx][0],ptr,a[idx][1][0])):
            true_ans = max(true_ans,ans)
        a[idx][0] = 'nop'

print(true_ans)



