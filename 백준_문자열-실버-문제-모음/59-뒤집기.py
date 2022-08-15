S = input()
case1 = S.count('01')
case2 = S.count('10')
if case1 == 0:
    print(str(case2))
elif case2 == 0:
    print(str(case1))
else:
    print(str(max(case1,case2)))
#s = input()

# zNum = 0
# oNum = 0

# for i in range(len(s) - 1) :
#     if s[i] != s[i+1] and s[i] == "0" :
#         zNum += 1
#     elif s[i] != s[i+1] and s[i] == "1" :
#         oNum += 1
# print(max(oNum, zNum))
