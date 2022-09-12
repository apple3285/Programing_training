# 백준- https://www.acmicpc.net/problem/5636
import math
import sys
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

for line in sys.stdin:
    line = line.rstrip()
    max_prime_number = 0
    if line == "0":
        break
    for i in range(1,len(line)+1):
        start = 0
        while (start+i<len(line)+1):
            num = int(line[start:start+i])
            if is_prime_number(num) and max_prime_number<num and 2<= num <100000:
                max_prime_number = num
            start+=1
    print(max_prime_number)
