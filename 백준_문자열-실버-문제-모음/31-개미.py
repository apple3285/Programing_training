# 백준 - 개미 (https://www.acmicpc.net/problem/3048)
n1,n2= map(int,input().split())
n1_ants = input()
n2_ants = input()
T = int(input())

#T = 0일때 개미 상태
ants = [ant for ant in n1_ants[::-1] + n2_ants]
# 각 개미들이 향하는 방향 -1은 왼쪽, +1은 오른쪽
direction =[-1]*n1 + [1]*n2 
# now: 0 현재 T  
# start~end : 뛰어넘을 수 있는 개미가 있는 위치
now = 0
start = 0
end = len(ants)-1
while (now<T):
    #만약 맨 앞 또는 맨 뒤 개미의 방향이 1이나 -1이라면 더 이상 뛰어넘을 개미가 없으므로 확인하지 않음
    if direction[start] == 1:
        start+=1
    if direction[end] == -1:
        end-=1
    index = start
    # 뛰어넘기가 가능한 개미들을 확인 
    # 만약 앞뒤 개미가 반대 방향으로 향하고 있다면 둘의 위치를 바꿈
    # 위치가 바뀐 개미들은 더 이상 바뀔 수 없으므로 인덱스를 1 더 증가시킴
    while (index < end):
        if direction[index] == direction[index+1]*-1:
            ants[index],ants[index+1] = ants[index+1],ants[index]
            direction[index],direction[index+1] = direction[index+1],direction[index]
            index+=1
        index+=1
    now+=1
print("".join(ant for ant in ants))
