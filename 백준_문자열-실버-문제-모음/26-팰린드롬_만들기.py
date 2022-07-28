#백준 팰린드롬 만들기 https://www.acmicpc.net/problem/1213

import collections
name = input()
# 이름에 쓰인 문자와 문자 개수 저장
count = collections.Counter(name)

# 주어진 문자열로 팰린드롬을 만들 수 있는지 확인하는 함수
# 만약 문자 개수가 홀수인 경우가 1개가 넘는다면 팰린드롬을 만들 수 없음
def is_palindrome_possible (count):
    odd_count = 0
    for cnt in count.values():
        if cnt % 2 == 1: 
            odd_count += 1
        if odd_count >1:
            return False
    return True

#팰린드롬 만드는 함수
def make_palindrome(count,name):
    #팰린드롬 결과를 저장할 문자열
    result = ""
    # 팰린드롬을 만들때 사용할 문자 리스트 
    str_list = [n for n in name]
    #홀수번 등장하는 문자를 결과 가장 가운데에 올 수 있도록 먼저 result에 삽입하고 문자 리스트에서 해당 문자 하나를 제거
    for string,cnt in count.items():
        if cnt % 2 == 1:
            result = string 
            str_list.remove(string)
    #문자 리스트를 정렬
    str_list.sort()
    #문자 리스트가 소진될때 까지 뒤에서 빼서 결과 문자열의 앞과 뒤에 추가해줌
    while(str_list):
        result = str_list.pop() +result + str_list.pop()
    print(result)

if is_palindrome_possible(count):
    make_palindrome(count,name)
else:
    print("I'm Sorry Hansoo")
