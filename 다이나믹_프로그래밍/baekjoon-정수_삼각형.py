#백준 - 정수 삼각형
n = int(input())
data =[]
#이차원 배열로 정수 삼각형 수 저장
for i in range(n):
    data.append(list(map(int,input().split())))
#현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽의 있는 수 중 더 큰 수를 더해줌
#만약 선택된 수가 현재 층에서 첫번째 수이거나 마지막 수인 경우 대각선 오른쪽 또는 대각선 왼쪽 수만 더함
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            data[i][j] += data[i-1][j]
        elif j == i:
            data[i][j] += data[i-1][j-1]
        else:
            data[i][j] +=max(data[i-1][j-1],data[i-1][j])
print(max(data[n-1]))
