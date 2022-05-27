# 백준 동전 0 문제

N, K = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
    
#동전 리스트를 오름차순 정렬
coin.sort()
# 큰 동전부터 사용하여 K를 동전으로 나누어서 나머지 값이 k이면 k보다 동전이 큰것이므로 다음 반복으로 넘어가기
#                                           나머지 값이 K보다 작고 0과 같거나 크면 동전으로 k 만들 수 있으므로 몫 저장
result = 0
for i in range(N-1,-1,-1):
    if K%coin[i] == K :
        continue
    elif K> K%coin[i] >= 0 :
        result +=  K//coin[i]
        K = K%coin[i]
        
print(result)
