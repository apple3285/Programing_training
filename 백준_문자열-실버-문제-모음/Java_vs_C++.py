# 백준 3613 : Java vs C++ ( https://www.acmicpc.net/problem/3613 )
name = input()

def change_to_java_style(name):
    # cpp 스타일의 이름이지만 예외인 경우는 에러 출력
    if name[0]=="_" or name[-1] =="_" or "__" in name:
        return "Error!"
    #현재 문자의 다음 문자를 대문자로 바꾸기 위해 사용하는 변수
    upper_check = 0
    result =""
    #이름의 한 문자씩 확인하여 현재 문자가 "_"인 경우 다음 문자를 대문자로 바꿈
    for char in name:
        if char == "_":
            upper_check = 1
            char=""
        elif upper_check :
            upper_check = 0
            char = char.upper()
        result+=char

    return result

def change_to_cpp_style(name):
    result =""
    # 이름의 한 문자씩 확인하여 현재 문자가 대문자인 경우 소문자로 바꾸고 앞에 "_"를 붙임
    for char in name:
        if char.isupper():
            char = "_"+char.lower()
        result+=char
    return result
        
    
if name.replace("_","").islower() and "_" in name: #CPP인 경우
    print(change_to_java_style(name))
elif name[0].islower() and name.isalpha(): #java인 경우 (반례 a_B)
    print(change_to_cpp_style(name))
else:
    print("Error!")
