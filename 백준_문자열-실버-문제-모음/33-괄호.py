# 백준 - 괄호 (https://www.acmicpc.net/problem/9012)
import sys

T = int(input())
for i in range(T):
    string = input()
    stack =[]
    is_VPS = True
    for s in string:
        if s == "(" :
            stack.append(s)

        elif s == ")":
            if not stack:
                is_VPS =False  
                break
            elif s == ")":
                if stack[-1] =="(":
                    stack.pop()
                else:
                    is_VPS =False    
                    break  
   
        
    if is_VPS and not stack:
        print("YES")
    else:
        print("NO")
