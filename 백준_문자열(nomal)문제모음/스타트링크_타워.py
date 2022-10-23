# test case는 맞지만 틀렸습니다 나옴 
# https://www.acmicpc.net/submit/1089/50864008
import sys
input = sys.stdin.readline

data = "###...#.###.###.#.#.###.###.###.###.### #.#...#...#...#.#.#.#...#.....#.#.#.#.# #.#...#.###.###.###.###.###...#.###.### #.#...#.#.....#...#...#.#.#...#.#.#...# ###...#.###.###...#.###.###...#.###.###"
num_dict = {}
for i in range(10):
    num_dict[i]=[]
for row in range(5):
    for num in range(10):
        num_dict[num].append(data[:3])
        data = data[4:]
#print(num_dict)

floor_cnt = int(input())
floor_data=[]
clean_floor_data = {}
for i in range(floor_cnt):
    clean_floor_data[i]=[]
for row in range(5):
    floor_data=input()
    column = 0

    for j in range(floor_cnt):
        clean_floor_data[j].append(floor_data[column:column+3])
        column+=4
#print(clean_floor_data)
possible_floor =[]
for cnt in range(floor_cnt):
    possible_floor_tmp =[]
    for i in range(10):
        for row in range(5):
            for column in range(3):
                check = True
                if clean_floor_data[cnt][row][column] == "#" and num_dict[i][row][column]==".":
                    #print(i)
                    check = False
                    break
            if not check:
                break
        if check:
            possible_floor_tmp.append(str(i))
    if possible_floor_tmp:
        possible_floor.append(possible_floor_tmp)
if len(possible_floor) == 0:
    print(-1)
    exit()
#print(possible_floor)
    
from itertools import product
possible_floor_lst = list(product(*possible_floor))
#print(possible_floor_lst)
floor_sum=0
for f in possible_floor_lst:
    floor_sum+=int("".join(f))

result = round(floor_sum/len(possible_floor_lst),10)
print(result)
        


                #안내판이 고장났을수도 . 아닐 수도 #  있음
                #입력 전구 "." = 정답 전구"#" -> 동일 가능
                #입력 전구 "." = 정답 전구"." -> 동일 가능
                #입력 전구 "#" = 정답 전구"." -> 동일 불가능
                #입력 전구 "." = 정답 전구"#" -> 동일 가능
