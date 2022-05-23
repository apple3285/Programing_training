def solution(s):
    length = len(s)
    answer = length
    half = int(length/2)
    for i in range(1,half+1):
        slices = []
        index = 0
        while(index < length):
            slices.append(s[index:index+i])
            index = index+i
        cnt=1
        result = ""
        for i in range(len(slices)-1):
            if slices[i] == slices[i+1] :
                cnt+=1
            else:
                if cnt > 1:
                    result+=str(cnt)
                result+=slices[i]
                cnt = 1
        if cnt > 1:
            result+=str(cnt)
        result+=slices[-1]
        
        if answer > len(result):
            answer = len(result)
            
    return answer
