# 백준 - 가장 긴 증가하는 부분 수열

# dp = A[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
n = int(input())
A = list(map(int, input().split()))
dp = [1 for i in range(n)]
#현재 위치(i)보다 이전에 있는 원소(j)가 작다면 , 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
