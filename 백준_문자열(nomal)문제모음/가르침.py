N, K = map(int,input().split())
start = 'anta'
end = 'tica'
base = set(start+end)
words =[]
for i in range(N):
    words.append(list(input()))

if K<=5:
    print(0)
    exit()

remain_char = []
for word in words:
    remain_char.append(set(word)-base)
K -= 5

remove_char = []
while(K>0):
    remain_dict = {}
    for char_list in remain_char:
        length = len(char_list)
        for char in char_list:
            if char in remove_char:
                continue
            if length in remain_dict.keys():
                if char in remain_dict[length].keys():
                    remain_dict[length][char] += 1
                else:
                    remain_dict[length][char] = 1
            else:
                remain_dict[length] = {char : 1}
    min_cnt = min(remain_dict.keys())
    remove_char.append(max(remain_dict[min_cnt].keys(), key = lambda k : remain_dict[min_cnt][k] ))
    K-=1
result=0
for char_list in remain_char:
    if set(remove_char) >= char_list:
        result+=1
print(result)
