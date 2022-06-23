#백준 - 덩치 ( https://www.acmicpc.net/problem/7568 ) 
N = int(input())
data = []
#몸무게와 키 데이터 입력받아서 이중 리스트에 저장
for i in range(N):
    data.append(list(map(int,input().split())))
rank_list =[]
#모든 사람의 키와 몸무게를 비교하여 현재 사람보다 비교 대상의 키와 몸무게가 더 크다면 현재 사람의 등수를 1 증가
for target in  data:
    x,y = target[0],target[1]
    rank = 1
    for compare in data:
        x_, y_ = compare[0],compare[1]
        if x_ > x and y_ > y :
            rank +=1
    rank_list.append(rank)

print(" ".join(str(r) for r in rank_list))
