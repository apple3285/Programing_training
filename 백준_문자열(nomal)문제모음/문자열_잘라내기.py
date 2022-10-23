#https://www.acmicpc.net/submit/2866/50865484
import sys
input= sys.stdin.readline

r ,c = input().split()
r,c = int(r),int(c)
data = ["" for i in range(c)]

for i in range(r):
    row_data = input()
    for j in range(c):
        data[j]+=row_data[j]
count = 0        

while(1):
    tmp_data = [str[1:] for str in data]
    if len(set(tmp_data))!= c:
        break
    data = tmp_data
    count+=1

print(count)
