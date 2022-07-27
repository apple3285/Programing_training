#백준 - 30 (https://www.acmicpc.net/problem/10610)
#배수 판정법을 사용한 풀이
#3의 배수 : 모든 자리의 수의 합이 3의 배수 /10의 배수 :일의 자리의 수가 0
num = [int(n) for n in input()]
if 0 not in num or sum(num) % 3 != 0:
    print(-1)
    exit()
num.sort(reverse=True)
str_num=list(map(str,num))
print(''.join(str_num))


#순열을 사용한 풀이 - 메모리 초과 
#주어진 수로 순열을 사용하여 후보를 만들고 30의 배수인지 확인하는 방식
#입력 범위가 10만인데 이를 모두 순열로 만들면 시간이 많이 걸림
# import itertools
# num = [n for n in input()]
# int_num = list(map(int,num))
# if "0" not in num or sum(int_num) % 3 != 0:
#     print(-1)
#     exit()
# else:
#     num.remove("0")
# nums = list(map("".join, itertools.permutations(num,len(num))))
# nums.sort(reverse=True)
# for now in nums:
#     if int(now) %3 == 0:
#         print(now+"0")
#         exit()

# print(-1)
