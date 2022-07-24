#백준 1969 : DNA (https://www.acmicpc.net/problem/1969)
from collections import Counter

N,M = map(int,input().split())
#DNA 문자열을 저장하는 리스트
DNA_list =[]
for i in range(N):
    DNA_list.append(input())

result_DNA =''
hamming_distance=0
#문자열의 길이 만큼 각 위치의DNA 문자를 확인하여 많이 등장하면서 알파벳이 앞에 있는 문자를 구함
#해당 문자는 구하려는 문자열의 해당 위치 문자로 사용하고 남은 문자들의 등장 수는 더하여 Hamming Distance에 추가
for location in range(M):
    string =""
    for DNA in DNA_list:
        string+=DNA[location]
    #Conter는 정렬되지 않고 문자의 등장 수만 반환하기 때문에 문자열을 정렬한 다음에 Conter 사용
    counts = Counter(''.join(sorted(string))	)
    result_DNA+=counts.most_common()[0][0]
    for i in counts.most_common()[1:]:
        hamming_distance+=i[1]

print(result_DNA)
print(hamming_distance)
