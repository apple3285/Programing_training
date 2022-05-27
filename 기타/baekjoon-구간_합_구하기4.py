N ,M = map (int, input().split())

numbers = list(map(int, input().split()))
i_j_list =[]
for m in range(M):
    i_j = list(map(int,input().split()))
    i_j_list.append(i_j)

#입력 받은 숫자 리스트의 앞 숫자들의 값을 누적하여 합한 값을 현재 요소에 저장
prefix_sum = [0]
numbers_sum = 0
for number in numbers:
    numbers_sum += number
    prefix_sum.append(numbers_sum)
#위의 누적 합 리스트를 사용하여 주어진 구간의 합을 출력
for i_j in i_j_list:
    i , j = i_j[0], i_j[1]
    print(prefix_sum[j] - prefix_sum[i-1]) 
