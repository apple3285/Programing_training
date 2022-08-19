#https://www.acmicpc.net/problem/1026
N =int(input())
list1 = []
list2 = []
list1 =list(map(int,input().split()))
list2 =list(map(int,input().split()))
list1.sort()
list2.sort(reverse=True)
result = 0
for i in range(N):
    result += list1[i]* list2[i]
print(result)
