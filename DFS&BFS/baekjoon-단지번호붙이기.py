from collections import deque
N = int(input())
m = []

for n in range(N):
    m.append(list(map(int, input())))

def bfs(graph,root):
    cnt = 1
    m[root[0]][root[1]] = 2
    Q = deque([root])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            now_x, now_y = x + dx[i], y + dy[i]
            if 0 <= now_x < N and 0 <= now_y < N:
                if m[now_x][now_y] == 1:
                    m[now_x][now_y] = 2
                    cnt+=1
                    Q.append((now_x, now_y))
    return cnt
                    
result =[]                   
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            result.append(bfs(m,(i,j)))

print(len(result))
for r in sorted(result):
    print(r)
