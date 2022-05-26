#백준 18405번 - 경쟁적 전염
from collections import deque
#입력 받기
N, K = map(int, input().split())
m =[]
viruses = []
for _ in range(N):
    row = list(map(int, input().split()))
    m.append(row)
    viruses+=row

S,X,Y = map(int,input().split())

#시험관의 모든 바이러스  종류 리스트 만들기
viruses = sorted(list(set(viruses)))

# 너비 우선 탐색을 통해 매초 각 바이러스 증식
##1. 시험관의 모든 칸을 확인하며 바이러스가 존재하는 위치를 큐에 삽입(번호가 낮은 종류의 바이러스 순으로)
q = deque([])
for virus in viruses[1:]:
    for i in range(N):
        for j in range(N):
            if m[i][j] == virus:
                q.append([i,j,virus])
#2. 큐에 있는 현재 바이러스가 존재하는 위치를 큐에서 제거하며 해당 바이러스가 위 아래 왼쪽 오른쪽에 증식 가능하다면 증식하고 증식한 위치를 큐에 삽입, S초 만큼 반복"""
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for s in range(S):
    q_len = len(q)
    for _ in range(q_len):
        now = q.popleft()
        for i in  range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if m[nx][ny] == 0:
                    m[nx][ny] = now[2]
                    q.append([nx,ny,now[2]])
print(m[X-1][Y-1])
