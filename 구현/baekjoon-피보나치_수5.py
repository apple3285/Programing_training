#백준 - 피보나치5( https://www.acmicpc.net/problem/10870 )
n = int(input())
#피보나치수 0번째와 1번째가 저장된 리스트
fibo = [0,1]
#n번째 피보나치 수 까지 계산
for i in range(2, n+1):
    fibo.append(fibo[i-1]+fibo[i-2])
    
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(fibo[-1])
