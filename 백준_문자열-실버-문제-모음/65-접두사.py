#https://www.acmicpc.net/problem/1141
n = int(input())
words = []
for _ in range(n):
      words.append(input())
words.sort(reverse=True)
X =[]
for word in words:
      check = True
      for x in X:
            if x.startswith(word):
                  check = False    
      if check:
            X.append(word)
print(len(X))
