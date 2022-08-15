R, C = map(int, input().split())
puzzle = []
for _ in range(R):
    row = list(input())
    puzzle.append(row)
words = puzzle
for i in range(C):
    word =[]
    for j in range(R):
          word.append(words[j][i])
    words.append(word)

clean_words =[]
for word in words:
      temp = ""
      for w in word:
            if w != "#":
                  temp+=w
            else:
                  if temp and len(temp)>=2:
                    clean_words.append(temp)
                    temp = ""
                  else:
                        temp = ""
      if temp and len(temp)>=2:
            clean_words.append(temp)
      
if clean_words:
  print(sorted(clean_words)[0])
else:
  print("")
