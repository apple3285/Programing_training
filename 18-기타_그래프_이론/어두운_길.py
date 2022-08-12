"""
A. 문제
한 마을은 N개의 집과 M개의 도로로 구성되어 있다. 
각 집은 0번부터 N-1번까지의 번호로 구분된다. 
모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다.

정부에서 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 
결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 한다. 
마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하라.

a. 예를 들면.
예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 하면, 하루 동안 이 가로등을 켜기 위한 비용은 7이다.

b. 입력 조건
첫째 줄에 집의 수 N (1 <= N <= 200,000)과 도로의 수 M (N-1 <= M <= 200,000)이 주어진다.
다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X, Y, Z가 주어지며, 공백으로 구분한다. (0 <= X, Y < N) 이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 의미이다. 단, X와 Y가 동일한 경우는 없으며 마을을 구성하는 모든 도로의 길이 합은 $2^31$보다 작다.
c. 출력 조건
첫째 줄에 일부 가로등을 비활서오하하여 절약할 수 있는 최대 금액을 출력하라.

<입력 예시>
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

<출력 예시>
51
"""

#크루스칼 알고리즘을 사용 (https://freedeveloper.tistory.com/389?category=888096)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    x, y, z = list(map(int, input().split()))
    edges.append((x, y,z))
# 간선을 비용순으로 정렬
edges.sort(key = lambda x:x[2])



# 간선을 하나씩 확인하며
for edge in edges:
    a, b, cost = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        result += cost

print(result)
