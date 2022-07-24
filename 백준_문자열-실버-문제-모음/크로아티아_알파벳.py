#백준 2941 : 크로아티아 알파벳 ( https://www.acmicpc.net/problem/2941 ) 
word = input()
#크로아티아 알파벳을 변경하는 문자열들
alphabet_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt = 0
#문자열에서 위의 리스트에 해당하는 문자열이 있는 경우 몇 개 있는지 세고 문자열에서 모두 띄어쓰기로 치환
for alphabet in alphabet_list:
    if alphabet in word:
        cnt+= word.count(alphabet)
        word = word.replace(alphabet," ")
#남은 문자열에서 띄어쓰기를 제거하고 남은 문자열의 길이를 추가
cnt+=len(word.replace(" ",""))
print(cnt)
