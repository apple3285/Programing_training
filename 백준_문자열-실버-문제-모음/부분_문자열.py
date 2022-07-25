#백준 6550 : 부분 문자열 (https://www.acmicpc.net/problem/6550 )

import sys

for line in sys.stdin:
    s,t = line.rstrip().split()
    check_s = ""
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                check_s+=s[i]
                t = t[j+1:]
                break


    if check_s == s:
        print("Yes")
    else:
        print("No")

    
