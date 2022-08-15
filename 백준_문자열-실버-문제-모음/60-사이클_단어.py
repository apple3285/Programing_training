def BruteForcce(p,t):
  i = 0 #t의 검색 인덱스
  j = 0 #p의 검색 인덱스
  while i < len(t) and j < len(p):
    if t[i] != p[j]:
      i = i - j
      j = -1
    i += 1
    j += 1
  if j == len(p):
    return 1
  else:
    return 0
n = int(input())
words = []
check = [0]*n
for _ in range(n):
      words.append(input())
for i in range(len(words)):
      text = words[i]
      for j in range(i+1,len(words)):
            pattern = words[j]
            if BruteForcce(pattern,text) == 0:
                  check[j]+=1

print(len(set(check)))

  
