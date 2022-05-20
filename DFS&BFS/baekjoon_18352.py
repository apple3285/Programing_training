#백준 18352번- 특정 거리의 도시 찾기
import sys
input=sys.stdin.readline
N , M , K , X = map(int,input().split())

#dictionary로 key(출발 도시): value(도착 도시)와 같이 저장
city = {}
for i in range(M):
    start, end = map(int,input().split())
    if start in city.keys():
        city[start].append(end)
    else:
        city[start] = [end]


from collections import deque
#너비 우선 탐색을 진행하면서 도시를 방문 result 딕셔너리에 출발도시 부터의 거리 저장  
def bfs(root,graph,max_dist):
    visited = []
    q =deque([root])
    result = {}
    result[root] = 0
    while q:
        now = q.popleft()
        if now not in visited:
            visited.append(now)
            if now in graph.keys():
                candidate = list(set(graph[now])-set(visited))
                q += candidate
                for c in candidate:
                    if c not in result.keys(): 
                        result[c] = result[now]+1
        if result[c] > max_dist:
            break
    return result
           

city_distance = bfs(X,city,K)
result = []
for key, value in city_distance.items():
    if value == K:
        result.append(key)
if result:
    for r in sorted(result):
        print(r)
else:
    print(-1)
