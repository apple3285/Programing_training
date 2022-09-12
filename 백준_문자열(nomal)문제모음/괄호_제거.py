#https://www.acmicpc.net/problem/2800

from itertools import combinations
f = input()
stack =[]
bracket_indexs =[]
for i in range(len(f)):
    if f[i] == "(":
        stack.append(["(",i])
    elif f[i] == ")":
        if stack[-1][0] == "(":
            bracket_indexs.append((stack.pop()[1],i))
        else:
            stack.append([")",i])

combi = []
for i in range(1,len(bracket_indexs)+1):
    combi+=list(combinations(bracket_indexs,i))
result =[]
for c in combi:
    now = list(f)
    for index in c:
        now[index[0]]=""
        now[index[1]]=""
    result.append("".join(now))
result = list(set(result))
result.sort()
for r in result:
    print(r)

