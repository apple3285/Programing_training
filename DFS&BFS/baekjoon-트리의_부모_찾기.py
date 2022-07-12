#백준 - 트리의 부모 찾기
#방문했던 노드를 리스트에 저장하고 확인한 후 탐색하는 방식 O(n)이 걸림-> 시간초과
#25번째 줄 처럼 수정하여 시간 줄임 해결
from collections import deque
N = int(input())
graph={}
#입력받기
for i in range(N-1):
    node1 , node2 = map(int,input().split())
    if node1 in graph.keys():
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    if node2 in graph.keys():
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]

def BFS(root , graph):
    parent_list = [0]*(N+1)
    check = [False]*(N+1)
    queue = deque([root])
    while(queue):
        now = queue.popleft()
        if check[now]==False:
            check[now] = True
            for next in graph[now]:
                if parent_list[next] == 0:
                    parent_list[next] = now
                queue.append(next)
    return parent_list

result = BFS(1,graph)
for parent in result[2:]:
    print(parent)
