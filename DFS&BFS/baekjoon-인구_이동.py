#백준 16234번 - 인구 이동
#80%에서 시간 초과 수정 필요
from collections import deque
N, L, R = map(int,input().split())
g = []

for _ in range(N):
    row = list(map(int, input().split()))
    g.append(row)



    


def bfs(root,check):
    q = deque([root])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check[root[0]][root[1]] = 1
    same_bound = [[root[0],root[1]]]
    bound_sum =g[root[0]][root[1]]
    change_check = [0]
    while q:
        now = q.popleft()
        now_x , now_y = now[0],now[1]

        for i in range(4):
            pos_x = now_x + dx[i]
            pos_y = now_y + dy[i]
            if 0<=pos_x<N and 0<= pos_y <N and check[pos_x][pos_y] == 0 and L<=abs(g[now_x][now_y] - g[pos_x][pos_y])<=R:
                check[pos_x][pos_y] = 1
                q.append([pos_x,pos_y])
                same_bound.append([pos_x,pos_y])
                bound_sum += g[pos_x][pos_y]
                change_check.append(1)

    #print(check)
    #print(same_bound)
    each_bound = int(bound_sum/len(same_bound))
    for bound in same_bound:
        g[bound[0]][bound[1]] = each_bound
    return check,change_check

cnt = 0
while (1):
    check = [[0] * N for _ in range(N)]
    change=[]
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 :
                check,change_check = bfs([i,j],check)
                change.append(change_check)
    #print("현재 맵",g)
    #print("맵이 변화가 있었나?",change)

    if 1 in sum(change, []) :
        cnt+=1
    else:
        break

    # if 0 not in sum(check, []):
    #     break
    #print(cnt)
    
print(cnt)



    

