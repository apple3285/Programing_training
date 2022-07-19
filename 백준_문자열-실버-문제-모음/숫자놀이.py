#백준 - 숫자 놀이 https://www.acmicpc.net/problem/1755
M, N = map(int,input().split())
#입력 받은 정수를 숫자 단위로 하나씩 영어로 읽기 위해 필요한 숫자:영어 딕셔너리
num_str_matching_dict={'1':'one','2':'two','3':'tree','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}

#입력 받은 정수를 영어로 숫자 단위로 하나씩 읽어서 정수 : 숫자단위 영어로 저장 ->#{8: 'eight', 9: 'nine', 10: 'one zero', 11: 'one one'..., 28: 'two eight'}
num_to_str_dict ={}
for number in range(M,N+1):
    number_str = " ".join(str(number))
    num_to_str =""
    for string in number_str:
        if string != " ":
            num_to_str += num_str_matching_dict[string]
        else:
            num_to_str +=" "
    num_to_str_dict[number] = num_to_str

#숫자 단위 영어를 기준으로 정렬             
sorted_num_to_str_dict = sorted(num_to_str_dict.items(), key = lambda x : x[1])
#정렬된 순서대로 정수를 리스트에 저장
result = [num[0] for num in sorted_num_to_str_dict]
#한 줄에 10개씩 출력
#새로 알게된 aterisk(*) 리스트 압축 해제(https://mingrammer.com/understanding-the-asterisk-of-python/)
for i in range(0,len(result),10):
    print(*result[i : i+10])
