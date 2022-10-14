import sys
input = sys.stdin.readline

while(1):
    n = int(input())
    if n == -1:
        exit()
    m = []
    for i in range(n):
        nums = input().rstrip()
        m.append(list(int(num) for num in nums))
    check = [[0]*n for i in range(n) ]
    check[0][0]=1
    result = 0

    for x in range(n):
        now_x = x
        for y in range(n):
            now_y = y
            data = m[now_x][now_y]
            #if check[now_x][now_y] != 0:
            if check[now_x][now_y] != 0 and data != 0:
                #light
                if now_y + data < n:
                    check[now_x][now_y + data] =1
                    
                    if now_x == n-1 and now_y + data == n-1:
                        result +=1

                #down 
                if now_x + data < n:
                    check[now_x + data][now_y] =1
                
                    if now_x + data == n-1 and now_y == n-1:
                        result+=1
                    
 
        print(result)
