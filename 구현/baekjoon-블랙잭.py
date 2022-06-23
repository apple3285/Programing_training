#백준 - 블랙잭(https://www.acmicpc.net/problem/2798)
N, M = map(int, input().split())
cards = list(map(int,input().split()))

def combination(arr,r):
    wanted=[]
    if r==1:
        for i in arr:
            wanted.append([i])
    else:
        for i in range(len(arr)-r+1):
            for j in combination(arr[i+1:], r-1):
                wanted.append([arr[i]]+j)
    return wanted
#https://velog.io/@supergangho/2-Python-%EC%A1%B0%ED%95%A9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4

cards_combination = combination(cards,3)
min_val = 300000
result = -1
for card_list in cards_combination:
    cards_sum = sum(card_list)
    val = M - cards_sum
    if val >= 0 and min_val > val:
        min_val = val 
        result = cards_sum
print(result)
