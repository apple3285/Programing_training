# 백준 다각형의 넓이 문제
# 문제 못 풀고 풀이 방법 검색 후 구현
# 다각형의 면적을 구하는 신발끈 정리를 사용

point_cnt = int(input())
x_list = []
y_list = []

for i in range(point_cnt):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
    
x_list.append(x_list[0])
y_list.append(y_list[0])

result = 0
for i in range(point_cnt):  
    result += x_list[i] * y_list[i+1] 
    result -= x_list[i+1] * y_list[i]

print(round(1/2 * abs(result),1))
