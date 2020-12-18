from collections import deque

a = [ (e.replace(' ','').split('\n'))[0] for e in open("AOC_18.txt").readlines()]
print(a)
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
def modularize_two():
    if(len(stk_two)>0 and stk_two[len(stk_two)-1]=='+'):
        idx = len(stk_two)-1
        while(True):
            if(idx<0):
                break
            if(stk_two[idx] == '(' or stk_two[idx]=='*' or stk_two[idx].isdigit() ):#issue with this line here
                break
            else:
                stk_one.append(stk_two[idx])
                stk_two.pop()
                idx -= 1
#evaluates the reverse polish notation into a
def stack_reset():
    idx = 0
    while(idx < len(stk_one)):
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

def answer():
    #print(stk_two)
    for j in range(len(stk_two)-1,-1,-1):
        stk_one.append(stk_two[j])
    #print("STACK: ")
    #print(stk_one)
    stack_reset()
    #print(stk_one)
    return stk_one[0]


#converts expression to a readable Reverse Polish Notation
def process_input_part_one():
    res = 0
    for expression in a:
        expression = expression[len(expression)::-1]
        global stk_one,stk_two
        print(stk_one,stk_two)
        expression = [e for e in expression]
        for j in range(len(expression)):
            if(expression[j]==')'):
                expression[j]='('
            elif(expression[j]=='('):
                expression[j]=')'
        for char in range(len(expression)):
            if(expression[char].isdigit()):
                stk_one.append(int(expression[char]))
            else:
                stk_two.append(expression[char])
                if(len(stk_two)>0):
                    pass
            modularize()
        modularize()
        sv = answer()
        res += sv
        print(sv)

        stk_one = []
        stk_two = []
    return res
#operator precedence is assigned; addition takes precedence over multiplication
def process_input_part_two():
    res = 0
    for expression in a:
        expression = expression[len(expression)::-1]
        global stk_one,stk_two
        expression = [e for e in expression]
        for j in range(len(expression)):
            if(expression[j]==')'):
                expression[j]='('
            elif(expression[j]=='('):
                expression[j]=')'
        print(expression)
        for char in range(len(expression)):
            print(stk_one,stk_two)
            if(expression[char].isdigit()):
                stk_one.append(int(expression[char]))
            else:
                modularize()
                modularize_two()
                stk_two.append(expression[char])

        print(stk_one)
        sv = answer()
        res += sv
        print(sv)

        stk_one = []
        stk_two = []
    return res
        
#print(process_input_part_one())
print(process_input_part_two())


