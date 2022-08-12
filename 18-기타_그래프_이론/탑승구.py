"""
[문제]
공항에는 G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분됩니다.
공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 gi번째 (1 <= gi <= G) 탑승구 중 하나에
영구적으로 도킹해야 합니다. 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있습니다.

또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서
공항의 운행을 중지합니다. 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 합니다. 
비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하세요.

[입력 조건]
1. 첫째 줄에는 탑승구의 수 G (1 <= G <= 100,000)가 주어집니다.
2. 둘째 줄에는 비행기의 수 P (1 <= P <= 100,000)가 주어집니다.
3. 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 gi (1 <= gi <= G)가 주어집니다. 이는 i번째 비행기가
   1번부터 gi번째 (1 <= gi <= G) 탑승구 중 하나에 도킹할 수 있다는 의미입니다.

[출력 조건]
첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력합니다.

<입력 예시 1>
4
3
4
1
1
<출력 예시 1>
2

<입력 예시 2>
4
6
2
2
3
3
4
4
<출력 예시 2>
3
"""

#공부 코드 : https://unie2.tistory.com/734
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b


# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
# 부모 테이블 초기화
parent = [0] * (g + 1) 

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1) :
  parent[i] = i

result = 0
for _ in range(p) :
  # 현재 비행기의 탑승구의 루트 확인
  data = find_parent(parent, int(input()))
  if data == 0 : # 현재 루트가 0이라면, 종료
    break
  union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
  result += 1

print(result)

# #실패 코드
# g = int(input()) # 탑승구
# p = int(input()) # 비행기
# gi = []# 각 비행기가 도킹할 수 있는 탑승구의 정보 
# for i in range(p):
#     gi.append(int(input()))

# remain_g = [i for i in range(g)]

# gi.sort()
# print(gi)
# cnt = 0
# for now in gi:
#     if now <= remain_g[0]:
#         remain_g.pop(0)
#         cnt+=1
#     elif now >= remain_g[-1]:
#         remain_g.pop(0)
#         cnt+=1
#     else:
#         for i in range(len(remain_g)-1):
#             if remain_g[i] <= now <remain_g[i+1]:
#                 remain_g.pop(i)
#                 cnt+=1   


# print(cnt)


