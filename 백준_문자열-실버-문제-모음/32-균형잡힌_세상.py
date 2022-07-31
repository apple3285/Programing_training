import sys

for line in sys.stdin:
    string = line.rstrip()
    stack =[]
    if string == ".":
        break
    is_balance = True
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")" or s == "]":
            if not stack:
                is_balance =False  
                break
            elif s == ")":
                if stack[-1] =="(":
                    stack.pop()
                else:
                    is_balance =False    
                    break  
            elif s == "]":
                if stack[-1] =="[":
                    stack.pop()
                else:
                    is_balance =False  
                    break      
        
    if is_balance and not stack:
        print("yes")
    else:
        print("no")

