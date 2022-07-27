# 백준 - 피카츄 (https://www.acmicpc.net/problem/14405)
pikachu = input()
#바로 지우지 않고 "."으로 치환 - 삭제된 부분 앞뒤가 붙어서 발음되는 단어로 바뀔 수 있기 때문
pikachu = pikachu.replace("pi",".")
pikachu = pikachu.replace("ka",".")
pikachu = pikachu.replace("chu",".")
pikachu = pikachu.replace(".","")
if len(pikachu) == 0:
    print("Yes")
else:
    print("No")
