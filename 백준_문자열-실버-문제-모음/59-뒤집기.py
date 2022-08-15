S = input()
case1 = S.count('01')
case2 = S.count('10')
if case1 == 0:
    print(str(case2))
elif case2 == 0:
    print(str(case1))
else:
    print(str(max(case1,case2)))
