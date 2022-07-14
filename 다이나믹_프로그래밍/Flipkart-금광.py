#이차원 배열 요소 접근 인덱스가  햇갈림 공부 필요
'''
문제
n * m 크기의 금광이 있다. 금광은 1* 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라.
입력
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력
19
16
'''
T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    gold_list = list(map(int,input().split()))
    gold_map=[]
    now = 0
    while(now< n*m):
        gold_map.append(gold_list[now:now+m])
        now +=m

    for i in range(1,m):
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = gold_map[j-1][i-1]
            if j == n-1:
                left_down = 0
            else:
                left_down = gold_map[j+1][i-1]

            left = gold_map[j][i-1]

            gold_map[j][i]=gold_map[j][i] + max(left_down, left, left_up)

    result = 0
    for i in range(n):
        if result < gold_map[i][-1]:
            result = gold_map[i][-1]
    print(result)
