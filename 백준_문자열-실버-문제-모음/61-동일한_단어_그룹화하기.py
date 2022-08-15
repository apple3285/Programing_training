n = int(input())
cnt = 0
words =[]
for i in range(n):
  words.append(sorted(list(input())))
while words:
      target = words[0]
      if target in words:
            words = [word for word in words if word != target]
            cnt +=1
      else:
          words.remove(target)
          cnt+=1

print(cnt)
