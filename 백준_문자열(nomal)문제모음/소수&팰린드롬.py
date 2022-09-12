#https://www.acmicpc.net/problem/1747
# 첫번째 시도 : 틀림 -> 1이 소수가 아닌 것으로 수정해서 통과
import math
import sys
# 소수 판별 함수
def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def is_palindrome(x):
    reversed_x = str(x)[::-1]
    if str(x) == reversed_x:
        return True
    return False

num = int(input())
while(1):
    if is_prime_number(num) and is_palindrome(num):
        print(num)
        break
    num+=1
