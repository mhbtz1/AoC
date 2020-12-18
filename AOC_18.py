from collections import deque

a = [e.replace(' ','') for e in open("AOC_18.txt").readlines()]
stk_one = []
stk_two = []

def modularize():
    if(len(stk_two)>0 and stk_two[len(stk_two)-1]==')'):
        idx = len(stk_two)-1
        while(True):
            if(stk_two[idx]=='('):
                stk_two.pop()
                break
            else:
                if(stk_two[idx]==')'):
                    stk_two.pop()
                else:
                    stk_one.append(stk_two[idx])
                    stk_two.pop()
            idx -= 1
def stack_reset():
    idx = 0
    while(idx < len(stk_one)):
        #print(stk_one[idx])
        if(isinstance(stk_one[idx],int)):
            idx += 1
        else:
            if(stk_one[idx]=='+'):
                stk_one[idx-2] = stk_one[idx-2] + stk_one[idx-1]
                stk_one.pop(idx)
                stk_one.pop(idx-1)
                idx -= 1
            elif(stk_one[idx]=='*'):
                stk_one[idx-2] = stk_one[idx-2] * stk_one[idx-1]
                stk_one.pop(idx)
                stk_one.pop(idx-1)
                idx -= 1

#converts expression to a readable Reverse Polish Notation
def process_input():
    for expression in a:
        for char in range(len(expression)):
            #print(expression[char])
            if(expression[char].isdigit()):
                stk_one.append(int(expression[char]))
            else:
                print(stk_one)
                stk_two.append(expression[char])
                if(len(stk_two)>0):
                    print(stk_two)
            modularize()
        modularize()
        #print(stk_one)
        
process_input()
def answer():
    print(stk_two)
    for j in range(len(stk_two)-1,-1,-1):
        stk_one.append(stk_two[j])
    print("STACK: ")
    print(stk_one)
    stack_reset()
    print(stk_one)
    return stk_one[0]
answer()

