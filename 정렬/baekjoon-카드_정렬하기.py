#백준 1715번 - 카드 정렬하기 

import heapq
N = int(input())
#최솟값을 빨리 찾을 수 있는 힙을 사용
#힙에 입력값 삽입
cards = []
for _ in range(N):
    heapq.heappush(cards,int(input()))
result = 0

#힙에 원소가 1개 남을 때 까지 반복
while(len(cards)>1):
    # 가장 작은 2개의 카드 묶음 꺼내서 더하고 다시 힙에 삽입
    now = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards,now)
    result+=now
print(result)
