#백준 - 진짜 메시지 https://www.acmicpc.net/problem/9324

T = int(input())

for i in range(T):
    #메시지의 맨 마지막 문자가 세번째 등장하는 경우도 있으므로 한 번 더 삽입되었는지 확인하기 위해 알파벳 대문자가 아닌 문자를 임시로 넣어놓고 확인
    m = input()+"_"
    #현재 확인한 문자와 등장한 횟수를 저장하는 딕셔너리 
    dict={}
    #메시지가 진짜인지 가짜 나타내는 변수
    is_real = True
    now = 0
    #메시지의 문자를 하나씩 확인 
    while now < len(m):
        # 이미 등장했던 문자인 경우
        if m[now] in dict.keys():
            dict[m[now]]+=1
            #만약 현재까지의 등장횟수가 3이라면 다음 순서의 문자와 같은지 확인
            if dict[m[now]] == 3:
                #같지 않다면 메시지가 가짜인 경우
                if m[now] != m[now+1]:
                    is_real = False
                    break
                # 같다면 한번 더 문자가 삽입된 경우가 맞으므로 등장횟수를 초기화하고 다음 문자의 그 다음 문자부터 확인할 수 있도록 1을 더 증가 
                else:
                    dict[m[now]] = 0
                    now +=1
        #처음 등장한 문자인 경우 새롭게 저장
        else:
            dict[m[now]] = 1
        #다음 문자를 확인하기 위해 인덱스 증가
        now +=1

    if is_real:
        print("OK")
    else:
        print("FAKE")
