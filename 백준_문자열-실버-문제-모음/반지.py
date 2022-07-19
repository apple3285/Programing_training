target = input()
N = int(input())

cnt = 0
for i in range(N):
    ring = input()
    # 반지 시작을 다르게 읽을 수 있기 때문에 반지의 양 옆에 반지 문자열을 더 붙여준 다음 찾고자하는 문자열(target)이 존재하는지 확인
    ring = ring+ring+ring
    if target in ring :
        cnt+=1

# for i in range(N):
#     ring = input()
#     for j in range(10):
#         ring = ring[1:]+ring[0]
#         if target in ring :
#             cnt+=1
#             break

print(cnt)
