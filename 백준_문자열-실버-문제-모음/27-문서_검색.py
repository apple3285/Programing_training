#백준- 문서 검색
document = input()
target = input()
cnt = 0
while(1):
    if target in document:
        document = document.replace(target,"-",1)
        cnt+=1
        print(document)
    else:
        break
print(cnt)
