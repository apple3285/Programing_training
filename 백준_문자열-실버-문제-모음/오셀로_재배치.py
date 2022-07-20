#백준 - 오셀로 재배치
#몰라서 답지보고 공부 - https://jokerldg.github.io/algorithm/2021/06/29/othello.html
import sys

read = sys.stdin.readline

T = int(read().rstrip())

answers = []
result = 0
arr = []

for _ in range(T):
    N = int(read().rstrip())
    start = list(read().rstrip())
    goal = list(read().rstrip())

    for i in range(N):
        if start[i] != goal[i]:
            arr.append(start[i])

    if arr.count("B") >= arr.count("W"):
        result = arr.count("B")
    else:
        result = arr.count("W")
    answers.append(result)
    arr = []

for answer in answers:
    print(answer)
