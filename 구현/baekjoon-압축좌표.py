#백준- 압축좌표 ( https://www.acmicpc.net/status?user_id=apple3285&problem_id=18870&from_mine=1 )
N = int(input())
data = list(map(int,input().split()))
result_list =[]
#중복된 좌표를 제거하고 오름차순으로 정렬
clean_data = sorted(list(set(data)))
result_dict ={}
#딕셔너리에 각 좌표의 압축좌표를 저장 {원래 좌표 : 압축 좌표} 형식
for i in  range(len(clean_data)):
    result_dict[clean_data[i]] = i
#입력받은 좌표 순서대로 압축좌표를 출력
for x in data:
    print(result_dict[x],end= " ")
