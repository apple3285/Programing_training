#예제는 맞지만 시간 
import sys

input = sys.stdin.readline

while (1):
    m = int(input())
    if m == 0:
        break
    s = input()
    max_len = 1

    start,end =0,0
    
    for end in range(len(s)):
        if len(set(s[start:end])) > m:
            start += 1

        if max_len < len(set(s[start:end])):
            max_len = len(set(s[start:end]))
    print(max_len)  
