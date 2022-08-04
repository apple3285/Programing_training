
'''
선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있다. 
학생 N명의 성적은 모두 다른데 다음은 6명의 학생에 대하여 6번만 성적을 비교한 결과다.

1번 학생 → 5번 학생
3 → 4
4 → 2
4 → 6
5 → 2
5 → 4
A번 학생의 성적이 B번 학생보다 낮다면 화살표가 A에서 B를 가리키도록 한다.
위에 제시된 정보를 유추해서 순위를 정확히 알 수 있는 학생도 있고, 알 수 없는 학생도 있다. 
정리하면 4번 학생보다 성적이 낮은 학생은 3명이고, 성적이 높은 학생은 2명이므로 4번 학생의 성적 순위를 정확히 알 수 있지만 다른 학생은 정확한 순위를 알 수 없다.
학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 몇명인지 계산하는 프로그램을 구하시오.

<입력조건> 
첫째 줄에 학생들의 수 N(2 ≤ N ≤ 500)과 두 학생의 성적을 비교한 횟수 M(2 ≤ M ≤ 10,000)
다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B
Test Case
<입력>
6 6
1 5
3 4
4 2
4 6
5 2
5 4

<출력>
1
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict ={}
for i in range(1,n+1):
    dict[i] = [[],[]]

for i in range(m):
    low,high = map(int, input().split())
    dict[low][1].append(high)
    dict[high][0].append(low)
result = 0
for i in range(1,n+1):
    cnt=0
    check=[]
    check.extend(dict[i][0])
    for j in dict[i][0]:
        check.extend(dict[j][0])
    check.extend(dict[i][1])
    for j in dict[i][1]:
        check.extend(dict[j][1])
    if len(list(set(check))) == n-1:
        result+=1
print(result)


#플로이드 워셜 알고리즘을 사용한 풀이 (https://github.com/ndb796/python-for-coding-test/blob/master/17/2.py )
#플로이드 워셜 설명 ( https://freedeveloper.tistory.com/385?category=888096)
'''
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
 
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
 
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
 
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)
'''
