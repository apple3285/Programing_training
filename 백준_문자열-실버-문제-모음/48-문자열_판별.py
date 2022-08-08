# 코드 출처 : https://hazung.tistory.com/138
# 설명 https://sooooooyn.tistory.com/12
def sol(idx):
    global result
    if idx == len(S):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx+j]:
                    break
            else:
                sol(idx+len(A[i]))
    return
    
S = input()
A = []
dp = [0] * 101
for _ in range(int(input())):
    A.append(input())
result = 0
sol(0)
print(result)

# 실패한 코드 - A의 리스트 앞에서 부터 단어가 있다면 S에서 삭제해주는 방법 
# softwarecontest - [soft , software, contest] 인 경우 실패하게 됨
# import sys
ㅓ
# S = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# A = [sys.stdin.readline().rstrip() for i in range(N)]
# i=0
# while i < len(A):
#     if A[i] in S:
#         S = S.replace(A[i],"")
#         i = 0 
#     else:
#         i+=1
    
# if S == "":
#     print(1)
# else:
#     print(0)
