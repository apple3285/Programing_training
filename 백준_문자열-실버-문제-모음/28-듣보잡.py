#백준 - 듣보잡 ( https://www.acmicpc.net/problem/1764 )
N,M = map(int,input().split())
d = set(input() for i in range(N))
b = set(input() for j in range(M))
result = list(d & b)
result.sort()
print(len(result))
for r in result:
    print(r)
