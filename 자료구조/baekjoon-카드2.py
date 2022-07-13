from collections import deque

N = int(input())
cards = deque(list(range(1,N+1)))

while(len(cards)>1):
    cards.popleft()
    cards.append(cards.popleft())
print(cards.popleft())
