import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    tmp1 = input().rstrip()
    tmp2 = input().rstrip()

    if len(tmp1)>= len(tmp2):
        sn = tmp2 #small_num
        bn = tmp1
    else:
        sn = tmp1 #big_num
        bn = tmp2

    sn_int= -1
    while(1):
        
        if "{" == sn[-1]:
            break
        sn = sn[:-1]
        sn_int += 1

    while(sn_int>0):
        bn = bn[:-1]+"," +bn+ "}"
        sn_int -=1
    print(bn)
