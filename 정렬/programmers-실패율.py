#프로그래머스 - 실패율 (https://programmers.co.kr/learn/courses/30/lessons/42889)
#몈 가지 테스트 케이스에서 계속 실패함 -> "스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다."라는 조건을 놓침 for문 안에 else문을 추가하여 해결
from collections import Counter
def solution(N, stages):
    #dic : 스테이지와 해당 스테이지의 실패율이 담겨있는 딕셔너리
    dic = {}
    try_user = 0
    #가장 높은 단계의 스테이지에서부터 1 스테이지씩 내려오면서 실패율 계산
    #user:스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수, try_user: 스테이지에 도달한 플레이어 수
    for stage in range(N+1,0,-1):
        user = stages.count(stage)
        try_user +=user
        if try_user:
            False_percent = user/try_user
            dic[stage] = False_percent
        else:
            dic[stage] = 0
    # 마지막 스테이지까지 클리어한 사용자가 있는 경우 스테이지 배열에서 제거
    if max(dic) == N+1:
        dic.pop(max(dic))
    # 실패율이 높은 스테이지부터 내림차순으로 정렬, 만약 실패율이 같은 경우 오름차순으로 정렬
    dic = dict(sorted(dic.items(),key = lambda x : (x[1],-x[0]),reverse = True))
    #정렬된 딕셔너리의 키를 리스트로 만들기
    answer = list(dic.keys())
    
    return answer
