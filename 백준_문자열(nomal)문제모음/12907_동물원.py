#공부한 블로그 https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-12907-%EB%8F%99%EB%AC%BC%EC%9B%90
N = int(input())
arr = list(map(int, input().split()))

total = [0] * 41 #[0,0,0,0,0,0,0,0...]
ex_total = 2

for a in arr:
    total[a] += 1 #[2,2,1,0,0,0,0,0,...] 나보다 큰 애들은 인덱스 만큼 있어 , 각 인덱스에 저장된 값은 그렇게 대답한 동물 수

tmp = True
for cnt in total: #조건탐색
    if cnt > ex_total: # 인덱스가 뒤로 갈 수록 현재 인덱스에 저장된 값 보다 작아져야함 
        tmp = False
        break
    ex_total = cnt

if tmp:
    print(2 ** (total.count(2) + (1 if 1 in total else 0)))
else:
    print(0)
