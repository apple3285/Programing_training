import sys
input = sys.stdin.readline

nums = input()

def dfs(nums,index,path,paths,check):
    path.append(nums[index])
    check[index] = True

    if path

    if path[-1] == nums :
        return
        if path not in paths:
            paths.append(path)
            cnt+=1

    if index+1 < len(nums):
        dfs(nums,index+1,path,result)
    elif index -1 >= 0:
        dfs(nums,index-1,path,result)

result =[]
check = [False*len(nums)]
for num in nums:
    dfs(nums,0,[],[],check)
