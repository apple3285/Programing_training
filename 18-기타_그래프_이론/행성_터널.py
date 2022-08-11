# 크루스칼 알고리즘 (https://freedeveloper.tistory.com/389?category=888096)을 사용하여 시도
# 메모리 초과 : 한 행성에서 다른 행성과의 모든 간선을 만들어서 시도
#              크루티칼 알고리즘의 특성상 인접 노드를 사용하며 이 문제는 최소 경로만 찾으면 되기 때문에 필요 없음(# #https://www.acmicpc.net/board/view/10945)
#

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
n= int(input()) #행성의 개수
parent = [0] * (n + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))    


# 문제된 부분
# planets = []
# for _ in range(v):
#     x, y, z = map(int, input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#     planets.append([x,y,z])
# 모든 간선에 대한 정보를 입력 받기
# for i in range(v):
#     for j in range(i,v):
#         cost = min(abs(planets[i][0]-planets[j][0]),abs(planets[i][1]-planets[j][1]),abs(planets[i][2]-planets[j][2]))
#         # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#         edges.append((cost, i, j))


# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
