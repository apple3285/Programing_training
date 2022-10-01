string = input()
bomb = input()
bomb_len = len(bomb)
result =[]
for s in string:
    result.append(s)
    if ''.join(result[-bomb_len:]) == bomb:
        del result[-bomb_len:]

if result:
    print("".join(result))
else:
    print("FRULA")
