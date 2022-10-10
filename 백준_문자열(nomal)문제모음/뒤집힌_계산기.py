#예제 정답은 모두 출력하지만 제출하면 시간 초과
# 몫 계산 구현은 다른 코드 참고(https://chinpa.tistory.com/101)

priority = list(map(int,input().split()))
ex =  input()
prior_symbol_dict = {}
n = []
s = []
s_lst = [ '+', '-', '*', '/']

for i in range(0,4):
    prior_symbol_dict[priority[i]] = s_lst[i]

tmp = ""
for char in ex:
    if char in s_lst:
        s.append(char)
        if tmp!="":
            n.append(tmp.lstrip("0"))
            tmp =""
    else:
        tmp+=char
if tmp:
    n.append(tmp.lstrip("0"))


while s :
    for i in range(4,0,-1):
        now_s = prior_symbol_dict[i]
        for j in range(len(s)-1,-1,-1):
            if s[j] == now_s:
                s.pop(j)
                if now_s == "/":
                    now_s+="/"
                    n1,n2 = n.pop(j+1),n.pop(j)
                    tmp = eval(n1 +now_s+n2)
                    if (int(n1) > 0 and int(n2) < 0) or (int(n2) > 0 and int(n1) < 0):
                        tmp += 1
                else:
                    tmp = eval(n.pop(j+1) +now_s+n.pop(j))
                n.insert(j,str(tmp))

print(int(n[0]))
                
