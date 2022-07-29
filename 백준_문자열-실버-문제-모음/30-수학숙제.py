N = int(input())
result= []
for i in range(N):
    word = input()
    temp=""
    for now_str in word:
        if now_str.isdigit():
            temp+=now_str
        else:
            if temp:
                result.append(int(temp))
                temp=""
    if temp:
        result.append(int(temp))

result.sort()

for r in result:
    print(r)
