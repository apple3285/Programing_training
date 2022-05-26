#프로그래머스-블록 이동하기
#코드 출처 - https://github.com/ndb796/python-for-coding-test/blob/master/13/8.py
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
"""
내가 작성한 실패한 코드 분석
1. 경우의 수를 잘못 설정해서 예외를 모두 알 수가 없어서 해결하지 못함
   -> 위의 코드 같은 경우에는 이동(오/왼/위/아래)과 회전(가로인 경우/세로인 경우)로 경우의 수를 설정하여 코드가 깔끔 
      나는 회전하는 경우  로봇의 상태를 고려하지 않음
2. 함수를 만들어 해결하였다면 조금 더 쉬웠을것 같음
3. 나는 로봇의 좌표를 하나의 리스트에 저장했지만 따로 변수를 만들어 사용했다면 코드 작성이 수월했을듯
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
N = len(board[0])
check = [[0] * N for _ in range(N)]
print(check)
from collections import deque
from lzma import MF_BT3
start = [0,0,0,1]
q = deque([])
q.append(start)

ml = [-1,0,-1,0]
mr =[1,0,1,0]
mu = [0,1,0,1]
md = [0,-1,0,-1]
mt1 = [0,0,-1,1]
mt2 = [1,1,0,0]
mt3 = [0,0,-1,-1]
mt4 = [-1,1,0,0]
moves =[ml,mr,mu,md,mt1,mt2,mt3,mt4]
visited =[]
while q:
    if check[N-1][N-1] != 0:
        break
    print(q)
    now = q.popleft()
    if now not in visited:
        visited.append(now)
        now_time = max(check[now[0]][now[1]],check[now[2]][now[3]])+1
        print(now)
        for i in range(len(moves)):
            moved = [now[j]+moves[i][j] for j in range(4)]
            print(moved)
            if  N> moved[0] >= 0 and N> moved[1] >= 0 and  N>moved[2] >= 0 and  N> moved[3] >= 0:
                print("통과")
                if i == 4 and N >now[2]+1 and board[now[2]+1][now[3]] == 1:
                    break
                elif i == 5 and N >now[0]+1 and board[now[0]+1][now[1]] == 1:
                    break
                elif i == 6 and board[now[2]-1][now[3]] == 1:
                    break
                elif i == 7 and board[now[0]-1][now[1]] == 1:
                    break
                print("통과2")
                if board[moved[0]][moved[1]] == 0 and  board[moved[2]][moved[3]]==0:
                    q.append(moved)
                    print("통과3")
                    
                    if check[moved[0]][moved[1]] == 0:
                        check[moved[0]][moved[1]] = now_time
                    if check[moved[2]][moved[3]] == 0:
                        check[moved[2]][moved[3]] = now_time
        print(check)
"""
        
