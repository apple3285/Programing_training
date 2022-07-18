#문자열 뒤에 추가하는 것이 아니고 문자열 어디든 추가해서 팰린드롬을 만들어도 된다고 문제 착각함 다시 풀어야함
import sys
string = sys.stdin.readline().rstrip()

def edit_dist(str1, str2) :
    n = len(str1)
    m = len(str2)

    # if str1 == str2[::-1]:
    #     return 0

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 초기 설정
    for i in range(1, n + 1) :
        dp[i][0] = i
    for j in range(1, m + 1) :
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1) :
        for j in range(1, m + 1) :
        # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입
            if str1[i-1] == str2[j-1] :
                dp[i][j] = dp[i-1][j-1]
        # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else : # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + dp[i][j-1]
    
    return dp[n][m]


string_len = len(string)
min_edit_dist = 50
for i in range(1,string_len):
    now_edit_dist = min(edit_dist(string[:i],string[:i-1:-1]),edit_dist(string[:i],string[:i:-1]))
    if now_edit_dist < min_edit_dist:
        min_edit_dist = now_edit_dist

if string_len == 1:
    print(1)
else:
    print(len(string)+min_edit_dist)
