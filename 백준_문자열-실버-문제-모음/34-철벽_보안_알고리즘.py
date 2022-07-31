
case = int(input())
for i in range(case):
    n = int(input())
    first_keys = input().split()
    second_keys = input().split()
    password = input().split()
    #{특정 문자의 1 공개키 위치 : 2 공개키 위치} 정보를 담은 딕셔너리를 만듦
    dict ={}
    for index in range(n):
        dict[second_keys.index(first_keys[index])] = index
    # 문자의 1,2 공개키 위치를 담은 딕셔너리를 사용하여 입력 받은 암호의 2 공개키 위치를 1 공개키 위치에 매칭시켜 result리스트에 저장
    result =["_"] * n
    for index in range(n):
        result[dict[index]] = password[index] 
    print(" ".join(result).rstrip())
