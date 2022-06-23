# 백준 - 소수찾기 ( https://www.acmicpc.net/submit/1978/44905948 )
N = int(input())
nums = list(map(int,input().split()))
result = 0
#check : 소수는 1 아닌 경우 0
#만약 1이면 소수가 아니므로 통과, 그 외의 경우 2~ 해당숫자-1 까지의 수로 나누었을때 나머지가 0인 경우 소수가 아님
for num in nums:
    if num ==1:
        continue
    check = 1
    for i in range(2,num):
        if num %i == 0 :
            check = 0
    if check:
        result+=1
print(result)
