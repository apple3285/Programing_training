# https://www.acmicpc.net/problem/5534
#공부한 코드 출처 :https://devlibrary00108.tistory.com/428
import sys
input = sys.stdin.readline

def check(string):
    l = len(string)
    for start_idx in range(l):
        if string[start_idx] == name[0]:
            for end_idx in range(start_idx,l):
                if string[end_idx]==name[-1]:
                    avg_gap = (end_idx-start_idx)//(n-1)
                    cnt = 0
                    while cnt < n:
                        if string[start_idx+avg_gap*cnt]==name[cnt]:
                            cnt += 1
                            continue
                        break
                    else:
                        return 1
    return 0

N = int(input())
name = input().rstrip()
n = len(name)
kanbans = list(input().rstrip() for _ in range(N))
cnt = 0
for kanban in kanbans:
    cnt += check(kanban)
print(cnt)

# 실패한 코드 : 간판의 모든 문자열을 확인하며 일정한 간격을 이동하며 새로운 간판을 만드는 방법
# 예제는 잘 출력되지만 통과 못함
n = int(input())

name = input()
name_len = len(name)
boards = [input() for _ in range(n)]
result = []
cnt = 0
for board in boards:
      interval = [i for i in range(1,len(board)//name_len+2)]
      for start in range(len(board)):
            if board[start] == name[0]:
                  for i in interval:
                        temp =""
                        for j in range(start,len(board),i):
                              temp+=board[j]
                              if len(temp)==name_len:
                                    break
                        result.append(temp)
      if name in result:
            cnt+=1
      result = []

print(cnt)
