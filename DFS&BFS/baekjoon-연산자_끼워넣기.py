#백준 연산자 끼워넣기 문제
#DFS/BFS로 해결방법을 생각하지 못해서 다른 방법으로 해결
#다른 풀이 보면서 공부
from itertools import permutations

N = int(input())
nums = list(map(int,input().split()))
signs_cnt = list(map(int,input().split()))

# 각 연산자의 수 만큼 리스트에 저장
signs =[]
for idx,cnt in enumerate(signs_cnt):
    if idx == 0:
        signs.append(["+"]*cnt)
    elif idx == 1:
        signs.append(["-"]*cnt)
    elif idx ==2:
        signs.append(["*"]*cnt)
    elif idx ==3: 
        signs.append(["/"]*cnt)
signs = sum(signs,[])


# 모든 연산자를 가지고 만들 수 있는 순서 조합을 저장한 리스트 만들기(중복된 조합은 제거)
signs_list =[]
for signs in permutations(signs,len(signs)):
    signs_list.append(signs)
signs_list = list(set(signs_list))

# 모든 연산자 조합을 사용하여 수식 계산
result_list =[]
for signs in signs_list:
    result = int(eval(str(nums[0])+ signs[0]+ str(nums[1])))
    i = 1
    while i < N-1:
        result = int(eval(str(result)+ signs[i]+ str(nums[i+1])))
        i+=1
    result_list.append(result)

#최댓값과 최솟값 출력
print(max(result_list))
print(min(result_list))


## DFS를 사용한 방법 (출처 : https://github.com/ndb796/python-for-coding-test/blob/master/13/5.py ) 
# n = int(input())
# # 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())

# # 최솟값과 최댓값 초기화
# min_value = 1e9
# max_value = -1e9

# # 깊이 우선 탐색 (DFS) 메서드
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         # 각 연산자에 대하여 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
#             div += 1

# # DFS 메서드 호출
# dfs(1, data[0])

# # 최댓값과 최솟값 차례대로 출력
# print(max_value)
# print(min_value)
