#백준 4659 : 비밀번호 발음하기 (https://www.acmicpc.net/problem/4659)
#zoggax 출력 다름 
#wiinq 출력 다름
# 수정 필요

import sys

collections = ["a","e","i","o","u"]
for line in sys.stdin:
    password = line.rstrip()
    is_accept = False
    check_collection =password
    if password == "end":
        break
    for collection in collections:
        if collection in password:
            is_accept = True

    consonant_cnt = 0
    collection_cnt = 0
    consonant_max=0
    collection_max = 0
    pre_string = ""
    for string in password:
        if string in collections:
            collection_cnt+=1
            consonant_max = max(consonant_max, consonant_cnt)
            consonant_cnt = 0
        else:
            consonant_cnt+=1
            collection_max = max(collection_max, collection_cnt)
            collection_cnt = 0
        if pre_string == string:
            if string != "e" or string != "o":
                is_accept = False
    


    consonant_max = max(consonant_max, consonant_cnt)
    collection_max = max(collection_max, collection_cnt)
    if consonant_max > 2 or collection_max > 2:
        is_accept = False

    if is_accept:
        print("<%s> is acceptable."%password)
    else:
        print("<%s> is not acceptable."%password)


    

            

