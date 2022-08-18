# https://www.acmicpc.net/problem/2839 설탕배달

sugar = int(input())
cnt = 0
while(1):
	if sugar % 5 == 0:
		cnt += sugar//5
		break
	cnt += 1
	sugar -= 3

	if sugar<0:
		cnt = -1
		break
print(cnt)
