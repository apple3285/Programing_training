# https://www.acmicpc.net/problem/10384

import sys
from string import ascii_lowercase
 
n = int(sys.stdin.readline())
alpha_list = list(ascii_lowercase)
for i in range(n):
    case = sys.stdin.readline().rstrip().lower()
    cnt = []
    for alpha in alpha_list:
        cnt.append(case.count(alpha))
    if cnt.count(0)+cnt.count(1) +cnt.count(2) == 0:
        print("Case %d: Triple pangram!!!"%(i+1))
    elif cnt.count(0)+cnt.count(1) == 0:
        print("Case %d: Double pangram!!"%(i+1))
    elif cnt.count(0) == 0:
        print("Case %d: Pangram!"%(i+1))
    else:
        print("Case %d: Not a pangram"%(i+1))
