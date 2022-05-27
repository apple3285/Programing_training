#백준 DFS와BFS 
#그래프 탐색에 DFS BFS를 사용하여 해결
#입력 받아 딕셔너리에 저장 
from collections import deque
graph_list = { }
node , edge , root = input().split()
node , edge , root = int(node), int(edge) , int(root)

#입력 받은 정점 두 개를 딕셔너리에 key, valueㄹ값으로 저장(key는 간선의 출발 점, value는 간선의 도착 점을 의미)
#문제 에서 양방향 간선이 입력으로 주어지기 때문에 두가지 경우를 첫번째 if~else 문과 두번째 if~else 문에서 모두 저장해줌
for n in range(edge):
    node1,node2 = input().split()
    node1,node2 = int(node1),int(node2)
    if node1 not in graph_list.keys():
        graph_list[node1] = [node2]
    else:
        graph_list[node1].append(node2)
    if node2 not in graph_list.keys():
        graph_list[node2] = [node1]
    else:
        graph_list[node2].append(node1)

#깊이 우선 탐색 함수
#stack을 사용
# 다음 방문 가능한 정점이 여러개가 되는 경우 정점 번호가 작은 것을 먼저 방문해야하므로 stack 에 정점을 내림차순으로 넣어줌(stack에서는 마지막 요소가 먼저 pop)
def dfs (graph,root):
    visited =[]
    stack = [root]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            if now in graph.keys():
                stack += sorted(list((set(graph[now]) - set(visited))),reverse=True)
    
    return visited

#너비 우선 탐색 함수
#queue를 사용
#다음 방문 가능한 정점이 여러개가 되는 경우 정점 번호가 작은 것을 먼저 방문해야하므로 큐에 정점을 오름차순으로 넣어줌( 큐는 먼저 들어간 것이 먼저 pop)
def bfs (graph,root):
    visited =[]
    queue = deque([root])

    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            if now in graph.keys():
                queue += sorted(list((set(graph[now])) - set(visited)))
    return visited


print(' '.join(str(x) for x in (dfs(graph_list,root))))
print(' '.join(str(x) for x in (bfs(graph_list,root))))
