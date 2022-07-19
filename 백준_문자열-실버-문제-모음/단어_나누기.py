word = input()
word_len = len(word)
words =[]
for i in range(0,len(word)):
    for j in range(i+1,len(word)-1):
        # 세 구간으로 나눈 뒤 문자열을 뒤집어 합침
        result = word[i::-1] + word[j:i:-1] + word[:j:-1]
        words.append("".join(result))

print(sorted(words)[0])
