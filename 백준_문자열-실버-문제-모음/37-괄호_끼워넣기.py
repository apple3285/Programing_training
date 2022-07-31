import sys
S = [s for s in sys.stdin.readline().rstrip()]
stack =[]
cnt = 0
for s in S:
    if s == "(":
        stack.append(s)
    else:
        if not stack: 
            cnt+=1
        elif stack[-1] == "(":
            stack.pop()
    
cnt += len(stack)
print(cnt)
