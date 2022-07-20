word1, word2 = input().split()

answer = []
for i in range(len(word2) - len(word1) + 1):
    count = 0
    for j in range(len(word1)):
        if word1[j] != word2[i + j]:
            count += 1
    answer.append(count)

print(min(answer))
