#백준 - 비슷한 단어
#다른 코드 공부 (출처 : https://fre2-dom.tistory.com/406)
import sys


n = int(sys.stdin.readline())
temp = [[] for _ in range(101)]
dic = [{} for i in range(101)]
cnt = 0

# 반복문을 통해 단어를 확인
for i in range(n):
    num = 0
    m = str(sys.stdin.readline()).rstrip('\n')

    # 반복문을 통해 알파벳을 확인하고
    # 그 알파벳을 수와 같이 딕셔너리형으로 추가한다.
    for j in m:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        # 현재 확인한 알파벳을 temp에 추가한다.
        temp[i] += dic[i][j]

# 반복문을 통해 같은 단어라면 카운트한다.
for i in range(n):
    for j in range(i + 1, n):
        if temp[i] == temp[j]:
            cnt += 1

print(cnt)




#실패한 코드

# N = int(input())
# target = [string for string in input()]
# target_set = set(target)
# cnt = 0
# for i in range(N-1):
#     word = [string for string in input()]
#     word_set = set(word)
#     is_similar = True
#     incorrect_spelling = 0
#     if len(word) == len(target):
#         for j in range(len(word)):
#             if word[j] != target[j]: 
#                 incorrect_spelling+=1
#         if 1<incorrect_spelling:
#              is_similar = False
#     else:
#         if 0<= len(word_set - target_set) <=1:
#             is_similar = False
            

#     if 0<= len(word_set - target_set) <=1 and incorrect_spelling<=1 :
#         cnt+=1




# print(cnt)
