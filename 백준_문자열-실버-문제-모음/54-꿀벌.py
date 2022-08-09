# https://www.acmicpc.net/problem/9733
import sys
data =[]
data = sum([line.split() for line in sys.stdin.readlines()],[])
work_dict = {}
work_cnt = len(data)
for work in data:
    if work in work_dict.keys():
        continue
    else:
        work_dict[work] = [data.count(work)]
for work,cnt in work_dict.items():
    work_dict[work].append(cnt[0]/work_cnt)
print(work_dict)

for work in ["Re","Pt","Cc","Ea","Tb","Cm","Ex"]:
    if work in work_dict.keys():
        print("%s %d %.2f"%(work,work_dict[work][0],work_dict[work][1]))
    else:
        print("%s 0 0.00"%(work))

print("Total %d 1.00"%(work_cnt))
