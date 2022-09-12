# 작성한 코드 : 런타임 에러
"""
from string import ascii_uppercase
k = int(input())
n = int(input())
end_position = input()
start_position = list(ascii_uppercase)[:k]
ladder =[]
for i in range(n):
    l = input()
    ladder.append(l)
    if l[0] == '?':
        question_mark = i

# 각 사람의 시작 위치에서 ? 전까지의 결과와 도착 위치에서 ? 전까지의 결과를 비교하기
# 두 결과를 비교해서 ?를 채우기
check = True
result = ["?"]*(k-1)
for i in range(k):
    up_position = i
    down_position = end_position.index(start_position[i])
    # 시작 위치에서 물음표의 전까지 이동한 결과 인덱스를 up_position에 저장
    for j in range(0,question_mark):
        if up_position == 0:
            if ladder[j][up_position] == "-":
                up_position +=1
        elif up_position == k-1:
            if ladder[j][up_position-1] == "-":
                up_position -=1
        else:
            if ladder[j][up_position] == "-":
                up_position+=1
            elif ladder[j][up_position-1] == "-":
                up_position-=1
    
    # 도착 위치에서 물음표의 전까지 이동한 결과 인덱스를 down_position에 저장
    for j in range(n-1,question_mark,-1):
        if down_position == 0:
            if ladder[j][down_position] == "-":
                down_position +=1
        elif down_position == k-1:
            if ladder[j][down_position-1] == "-":
                down_position -=1
        else:
            if ladder[j][down_position] == "-":
                down_position+=1
            elif ladder[j][down_position-1] == "-":
                down_position-=1


    #up_position과 down_position의 차이가 0또는 1이면 사다리를 놓거나 놓지 않음, 그 외에는 불가능한 상황이므로 x를 출력
    if abs(up_position - down_position)<=1:
      #만약 up_position과 down_position 위치가 같다면 사다리의 다리를 놓지 않음
        if up_position == down_position:
            if result[up_position] != "-" and result[up_position-1] != "-":
                result[up_position] = "*"
                if up_position > 0:
                    result[up_position-1] = "*"
            else :
                check = False
                break
        #만약 up_position > down_position 라면  down_position위치에 다리를 놓음
        elif up_position > down_position:
            if result[down_position]!="*":
                result[down_position] = "-"
            else :
                check = False
                break
         #만약 up_position < down_position 라면  up_position위치에 다리를 놓음
        elif up_position < down_position:
            if result[up_position]!="*":
                result[up_position] = "-"
            else :
                check = False
                break
    else:
        check = False
        break

# 사다리의 다리가 빈 경우 다리를 놓지 않음
result = "".join(result).replace("?","*")

if check:
    print(result)
else:
    print("x"*(k-1))
"""

# 공부한 코드 
# 출처:https://velog.io/@highero-k/%EB%B0%B1%EC%A4%80-2469-%EC%82%AC%EB%8B%A4%EB%A6%AC-%ED%83%80%EA%B8%B0-Python-%EA%B3%A8%EB%93%9C-5
k = int(input())
n = int(input())
end = list(input())
start = sorted(end)
ladder = [list(input()) for _ in range(n)]
ladderS = []
ladderE = []
#?를 기준으로 사다리 나누기
for i in range(len(ladder)):
  if ladder[i][0] == '?':
    ladderS = ladder[:i]
    ladderE = ladder[i+1:]
    break
# ????만나기 전까지 사디리 타고 내려오기
for lad in ladderS:
  for i in range(k-1):
    if lad[i] == "-":
      start[i],start[i+1] = start[i+1],start[i]
# 도착 지점에서 ????만나기 전까지 사다리 타고 내려오기
ladderE.reverse()
for lad in ladderE:
  for i in range(k-1):
    if lad[i] == "-":
      end[i],end[i+1] = end[i+1],end[i]
# 두 배열 비교해서 사다리 만들기
answer = []
for i in range(len(start)-1):
  if start[i]==end[i]:
    answer.append("*")
  else:
    if start[i]==end[i+1]:
      answer.append("-")
    elif i!=0 and start[i]==end[i-1]:
      answer.append("*")
    else:
      answer = ['x' for _ in range(k-1)]
      break
#정답
print(''.join(answer))

