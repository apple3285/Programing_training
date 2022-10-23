# https://www.acmicpc.net/submit/1990/50629379
# test case는 모두 맞지만 시간 초과 
import sys
import math
a,b = map(int, sys.stdin.readline().split())
primes = []
check = [False,False] + [True]*(b-1)
for i in range(2,int(math.sqrt(b))):
    if check[i]:
        primes.append(i)
    for j in range(2*i, b+1, i):
        check[j] = False
for num in range(a,b+1):
    check_prime = True
    for prime in primes:
        if prime == num:
            break
        elif num % prime == 0:
            check_prime = False
            break
    if check_prime and str(num)[::-1] ==str(num):
        print(num)

    
print(-1)
