#LCS 공부 : https://myjamong.tistory.com/317
#https://seongonion.tistory.com/96 기존의 2차원 배열을 3차원으로 늘려서 구현
import sys
input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()
seq_3 = input().rstrip()

x = len(seq_1)
y = len(seq_2)
z = len(seq_3)

arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]


for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if seq_1[i-1] == seq_2[j-1] and seq_2[j-1] == seq_3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = -1

for i in range(x+1):
    for j in range(y+1):
        ans = max(max(arr[i][j]), ans)

print(ans)

# 부분 문자열로 풀음 -> substring와 subsequence 다름 다시 풀어야됨
# str_lst = sorted([input() for i in range(3)],key = len)
# print(str_lst)

# short_str = str_lst[0]
# subseq_lst = []
# for length in range(1,len(short_str)+1):
#     index = 0
#     while(index+length<len(short_str)+1):
#         subseq_lst.append(short_str[index:index+length])
#         index+=1
# print(subseq_lst)
# while(1):
#     sub = subseq_lst.pop()
#     if sub in str_lst[1] and sub in str_lst[2]:
#         print(len(sub))
#         break
