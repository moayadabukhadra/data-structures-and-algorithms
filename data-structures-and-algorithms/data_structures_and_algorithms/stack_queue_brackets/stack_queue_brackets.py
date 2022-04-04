
from data_structures_and_algorithms.stack_and_queue.stack import Stack

def validate_brackets(s):
    if type(s)!=str:
        raise Exception("the input should be only strings")
    if s=="":
        raise Exception("the string cant be empty")
    brackets = ["[","{","(","]","}",")"]
    pairs = {"{": "}", "(": ")", "[": "]"}
    opens='({['
    closes=')}]'
    stack = Stack()
    only_brackets=""
    test=0
    for c in s:
        if c in brackets:
            only_brackets+=c
    
    for i in only_brackets:
        if i in opens and len(only_brackets)-test==1:
            return False , f"error unmatched opening {i} remaining."
        if i in opens:
            stack.push(i)
        
        elif stack.top and i == pairs[stack.peek()]:
             stack.pop()
        else:
            if stack.top and i != pairs[stack.peek()] :
                return False , f"error closing {i}. Doesn't match opening {stack.top.value}."
                   
            elif i in closes:
                return False , f"error closing {i} arrived without corresponding opening."
        test+=1
            

    return stack.top == None

