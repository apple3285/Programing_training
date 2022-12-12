s = input()
t = input()
check = 0
while(t!=""):
    if s == t:
        check = 1
        break
    elif t[-1] == "A":
        t= t[:-1]
    elif t[-1] == "B":
        t = t[:-1]
        t = t[::-1]

if check :
    print(1)
else:
    print(0)
