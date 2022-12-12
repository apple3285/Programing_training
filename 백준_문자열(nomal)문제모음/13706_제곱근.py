import sys
input = sys.stdin.readline
n = int(input())
left= 1
right = n

while 1:
    mid = (left + right) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        right = mid - 1
    elif mid ** 2 < n:
        left = mid + 1
