# https://www.acmicpc.net/problem/16171
S = input()
K = input()
result = ""
for s in S:
      if s.isalpha():
            result+=s
if K in result:
      print(1)
else:
      print(0)
