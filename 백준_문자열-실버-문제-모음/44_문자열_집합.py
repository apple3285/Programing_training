import sys

N,M = map(int,sys.stdin.readline().split())
sets =[]
checks = []
for i in range(N):
    sets.append(sys.stdin.readline().rstrip())

for j in range(M):
    checks.append(sys.stdin.readline().rstrip())
cnt=0
for check in checks:
    if check in sets:
        cnt+=1

print(cnt)
