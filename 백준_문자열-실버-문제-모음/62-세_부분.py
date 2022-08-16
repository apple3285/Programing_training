# https://www.acmicpc.net/problem/2993
# 코드 출처 : 부르트포스를 사용한 풀이 - https://jinho-study.tistory.com/1056
s = input()
li = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            li.append(t)
print(min(li))



# 틀린 코드 - 예제는 다 맞지만 체점에서 통과 못함
# word = input()

# ascii_list = [ord(w) for w in word]

# length = len(ascii_list)
# bound = []
# start = -1
# for end in length -2,length -1:
#       minimum = ord(word[end])
#       minimum_index = end
#       for index in range(end,start,-1):
#             if ascii_list[index] <= minimum:
#                   minimum = ascii_list[index]
#                   minimum_index = index
#       bound.append(minimum_index)
#       start = minimum_index

# bound.append(length-1)
# result = ""
# start = 0
# for end in bound:
#       now = end
#       while now >= start:
#             result+=word[now]
#             now-=1
#       start = end+1

# print(result)
