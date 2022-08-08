import sys

s = sys.stdin.readline()
s_list = []
for length in range(1,len(s)):
    index=0
    while (index+length < len(s)):
        s_list.append(s[index:index+length])
        index+=1
print(len(set(s_list)))
