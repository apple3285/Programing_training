# 부분 문자열로 풀음 -> substring subsequence 다름 다시 풀어야됨
# str_lst = sorted([input() for i in range(3)],key = len)
# print(str_lst)

# short_str = str_lst[0]
# subseq_lst = []
# for length in range(1,len(short_str)+1):
#     index = 0
#     while(index+length<len(short_str)+1):
#         subseq_lst.append(short_str[index:index+length])
#         index+=1
# print(subseq_lst)
# while(1):
#     sub = subseq_lst.pop()
#     if sub in str_lst[1] and sub in str_lst[2]:
#         print(len(sub))
#         break
