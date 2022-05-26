#백준 10825번 국영수 문제
N = input()
result =[]
for _ in range(int(N)):
    name , ko,en,ma = input().split()
    result.append([name,int(ko),int(en),int(ma)])

result.sort(key = lambda x :(-x[1],x[2],-x[3],x[0]))

for r in result:
    print(r[0])
