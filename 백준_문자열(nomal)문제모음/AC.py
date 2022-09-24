'''
#실패한 코드 - 시간 초과 
T = int(input())
for i in range(T):
    p= input()
    n = int(input())
    x = input().replace("[","")
    x = x.replace("]","")
    if x:
        x = list(map(int, x.split(",") ))
    check = True
    for f in p:
        if x :
            if f == "R":
                x = x[::-1]
            else :
                x = x[1:]
        else:
            check = False

    if check:
        result = "["
        for s in x:
            result += str(s)+","
        result = result[:-1] + "]"
        print(result)
    else:
        print("error")
'''  

# 공부한 코드 - https://it-garden.tistory.com/288
import sys
input = lambda : sys.stdin.readline().strip()
t = int(input())
for i in range(t):
    p = input()
    n = int(input())
    de = input()[1:-1].split(',')
    p = p.replace("RR","")

    r = 0
    f, b = 0,0
    for j in p:
        if j == "R":
            r+=1
        elif j == "D":
            if r % 2 == 0:
                f += 1
            else:
                b+=1
    if f + b <= n:
        de =de[f:n-b]

        if r % 2 == 1:
            print("["+",".join(de[::-1])+"]")
        else:
            print("["+",".join(de)+"]")
    else:
        print("error")
