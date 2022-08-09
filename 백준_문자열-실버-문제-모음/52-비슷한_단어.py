# https://www.acmicpc.net/problem/1411
import sys

n = int(sys.stdin.readline())
word_to_num_list = []
#등장하는 알파벳을 정수로 치환해서 같은 알파벳은 같은 정수를 같도록 word_to_num을 만들어서 비슷한 단어 쌍을 찾음
for i in range(n):
    word = sys.stdin.readline()
    dic = {}
    num = 0
    word_to_num = ""
    for s in word:
        if s in dic.keys():
            word_to_num+= dic[s]
        else:
            dic[s] = str(num)
            word_to_num += dic[s]
            num+=1
    word_to_num_list.append(word_to_num)

cnt = 0        
for i in range(len(word_to_num_list)):
    cnt += word_to_num_list[i+1:].count(word_to_num_list[i])
print(cnt)
