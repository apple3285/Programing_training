# 백준 11536 - 줄세우기 (https://www.acmicpc.net/problem/11536)
#파이썬 정렬 함수를 사용한 풀이
N = int(input())

names = [input() for i in range(N)]

increase_names = sorted(names)
decrease_names = sorted(names,reverse=True)

if increase_names == names:
    print("INCREASING")
elif decrease_names == names:
    print("DECREASING")
else:
    print("NEITHER")

#이름의 맨 앞글자의 아스키 코드를 사용한 풀이 - 틀림
#다시 생각해보니 맨 앞글자가 같은 경우 두번째 글자도 비교해주어야함
# N = int(input())

# names = [input() for i in range(N)]
# pre_ord = ord(names[0][0])
# increasing = 0
# decreasing = 0
# for name in names[1:]:
#     now_ord = ord(name[0])
#     if pre_ord < now_ord:
#         increasing +=1
#     elif pre_ord > now_ord:
#         decreasing +=1

# if increasing == 0:
#     print("DECREASING")
# elif decreasing == 0 :
#     print("INCREASING")
# else:
#     print("NEITHER")
