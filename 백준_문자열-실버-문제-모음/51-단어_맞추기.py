# 공부한 코드 ( https://hillier.tistory.com/102 )
import sys
input = sys.stdin.readline
def nextPermutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return False
 
    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1
 
    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result
 
 
T = int(input())
for _ in range(T):
    _input = list(input().rstrip())
    answer = nextPermutation(_input)
    if not answer:
        print("".join(_input))
    else:
        print("".join(answer))

# 실패한 코드 - permutations으로 조합을 만든 후 정렬하여 찾기
# 정답은 나오지만 메모리 초과
# import sys
# from itertools import permutations

# T = int(sys.stdin.readline())
# for i in range(T):
#     word = sys.stdin.readline().rstrip()
#     words = ["".join(w) for w in permutations(word)]
#     words = sorted(set(words))
#     word_index = words.index(word)
#     if word_index == len(words)-1:
#         print(word)
#     else:
#         print(words[word_index+1])
