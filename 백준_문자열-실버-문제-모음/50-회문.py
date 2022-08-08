# 못 풀음 컴파일 에러
import sys
T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline()
    print(len(string) % 2)
    if len(string) % 2 != 0:
        l ,r = len(string)//2-1 , len(string)//2
        print(l,r)
    else:
        l = r = int(len(string)//2)-1
        print(l,r)

    while(l=>0 and r<len(string)):
        
 # 공부한 코드 ( https://hillier.tistory.com/102 )
