# 백준- 최종순위 : https://www.acmicpc.net/problem/3665
# 출처 : https://github.com/ndb796/python-for-coding-test/blob/master/18/5.py
from collections import deque
# 테스트 케이스(Test Case)만큼 반복
for tc in range(int(input())):
    # 노드의 개수 입력 받기
    n = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n + 1) for i in range(n + 1)]

    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    print(graph)

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    print(indegree)

    # 위상 정렬(Topology Sort) 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내 사이클이 존재하는지 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i, end=' ')
        print()






# 실패한 코드 : 작년 정보와 현재 상대적 등수가 바뀐 정보를 어떻게 사용해서 위상정렬에 적용할지 고민해도 모르겠음
# 공부한 내용
#   그래프의 간선이 바로 전 후 등수의 노드 뿐만아니라 현재 노드와 비교했을 때 더 낮은 등수라면 이어지도록 그래프를 만들어야 함
#   코드대로 하면 정답이 나오지만 무슨 원리로 진입차수가 0인 경우를 큐에 삽입하고 연결된 노드들의 차수를 1씩 감소하는 과정에서 정렬되는지 이해가 안됨
# # 위상 정렬 알고리즘 - 출처 ( https://freedeveloper.tistory.com/390 )
# # 위상 정렬 함수
# def topology_sort():
#     result = [] # 알고리즘 수행 결과를 담을 리스트
#     q = deque() # 큐 기능을 위한 deque 라이브러리 사용

#     # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             q.append(i)

#     # 큐가 빌 때까지 반복
#     while q:
#         # 큐에서 원소 꺼내기
#         now = q.popleft()
#         result.append(now)
#         # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
#         for i in graph[now]:
#             indegree[i] -= 1
#             # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#             if indegree[i] == 0:
#                 q.append(i)

#     # 위상 정렬을 수행한 결과 출력
#     for i in result:
#         print(i, end=' ')


# # 노드의 개수와 간선의 개수를 입력 받기
# test_cnt = int(input())
# for i in range(test_cnt):
#     n = int(input()) # 팀의 수
#     ti = input().split() #작년에 i등을 한 팀의 번호
#     m = int(input())
#     a_b_list = []
#     for j in range(m):
#         a_b_list.append([map(int, input().split())])
#     print(a_b_list)
#     # 모든 노드에 대한 진입차수는 0으로 초기화
#     indegree = [0] * (n + 1)
#     # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
#     graph = [[] for i in range(n + 1)]
#     print(graph)

#     # 방향 그래프의 모든 간선 정보 (작년 등수를 기반으로 그래프를 생성)
#     for _ in range(n-1):
#         a, b = ti[n],ti[n+1]
#         graph[a].append(b) # 정점 A에서 B로 이동 가능
#         # 진입 차수를 1 증가
#         indegree[b] += 1
#     topology_sort()




