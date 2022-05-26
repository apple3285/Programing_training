#백준 18428번- 감시 피하기

N = int(input())
m = []
for _ in range(N):
    m.append(input().split()) # 초기 복도 리스트

temp =[[0] * N for _ in range(N)] # 장애물을 설치한 뒤의 복도 리스트

#선생님의 위치를 저장한 리스트 만들기
t_position =[]
for i in range(N):
    for j in range(N):
        if m[i][j] == 'T':
            t_position.append([i,j])

#선생님의 위치에서 사방을 확인하며 학생이 보이는지 확인하는 함수
def check():
    check = True
    #각 선생님의 위치에서 확인하기
    for position in t_position:
        now_x = position[0]
        now_y = position[1]
        result_x = ""
        result_y = ""
        #x축 또는 y 축을 고정해서 해당 행 또는 열을 확인
        for i in range(N):
            if temp[now_x][i] != "X":
                result_x+=temp[now_x][i]
            if temp[i][now_y] != "X":
                result_y+=temp[i][now_y]
        if "ST" in result_x or "TS" in result_x or "ST" in result_y or "TS" in result_y:
            check = False
            break
    return check

#깊이 우선 탐색을 이용해 장애물을 설치하면서, 매번 학생들이 선생님에게 보이지 않는지 확인 
def dfs(count):
    global result
    #장애물이 3개 설치된 경우
    if count ==3:
        for i in range(N):
            for j in range(N):
                temp[i][j] = m[i][j]
        check_result = check()
        if check_result:
            result = check_result
        return

    #빈 공간에 장애물 설치
    for i in range(N):
        for j in range(N):
            if m[i][j] =="X":
                m[i][j] = "O"
                count += 1
                dfs(count)
                m[i][j] = "X"
                count -=1
result = False
dfs(0)
if result:
    print("YES")
else:
    print("NO")
