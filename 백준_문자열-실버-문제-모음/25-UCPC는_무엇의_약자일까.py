# 백준 - UCPC는 무엇의 약자일까? (https://www.acmicpc.net/problem/15904)

string = input()
result =""
answer = "UCPC"

#입력 받은 문자열에서 대문자만 추출
for s in string:
    if s.isupper():
        result+=s
# 원하는 문자열과 같다면 
if result == answer:
    print("I love UCPC")
else:
    #추출한 대문자에서 "UCPC"가 순서대로 존재하는지 확인
    #축약할 수 있는 방법을 찾기 때문에 중간에 다른 대문자가 존재해도 "UCPC"가 순서대로 존재하면 가능
    is_possible = True
    for target in answer:
        index = result.find(target)
        if index != -1:
            result = result[index:]
        else:
            is_possible = False
        print(result)
    if is_possible:
        print("I love UCPC")
    else:
        print("I hate UCPC")
