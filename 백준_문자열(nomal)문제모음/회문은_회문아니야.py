'''
#실패한 코드 - 가장 긴 팰린드롬을 찾아서 남은 부분 중 가장 긴 부분을 찾음
#"ABCBACBCA"와 같은 경우 4가 출력되지만 9가 정답

#가장 긴 팰린드롬 찾는 함수 https://baechu-story.tistory.com/17
def longestPalindrome(s: str) -> str:
    
    #팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    #해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)

    return result


s = input()
result = longestPalindrome(s)
if len(result) == 1:
    print(len(s))
elif len(result)==len(s):
    str_uni = len(set(list(result)))
    if str_uni == 1:
        print(-1)
    else:
        print(len(result)-1)
else:
    temp = s.split(result)
    max_len = max(temp,key=len)
    print(len(max_len))
'''   
# 공부한 코드- https://fre2-dom.tistory.com/471
import sys


# 회문인지 판단
def solution(n):
    # 문자열이 짝수인지 홀수인지에 따라서 왼쪽 문자열과 오른쪽 문자열을 나눔.
    if len(word) % 2 == 0:
        left = word[0: len(word)//2 - n]
    else:
        left = word[0: len(word)//2 + 1 - n]

    right = word[len(word)//2:len(word) - n]

    # 왼쪽 문자열과 오른쪽 문자열이 똑같지 않으면 회문이 아님
    if left != right[::-1]:
        return True
    return False


word = list(map(str, sys.stdin.readline().strip()))

# 길이 n이 회문인지 확인
if solution(0):
    print(len(word))

# 길이 n-1이 회문인지 확인
elif solution(1):
    print(len(word) - 1)

# 회문!!!
else:
    print(-1)
