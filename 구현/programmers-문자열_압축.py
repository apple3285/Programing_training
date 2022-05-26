def solution(s):
    length = len(s)
    answer = length
    half = int(length/2)
    # 1~ 전체 문자열 절반까지 문자열 압축 단위를 1씩 늘려가면서 확인
    for i in range(1,half+1):
        slices = []
        index = 0
        #현재 압축 단위만큼씩 잘라서 리스트에 저장 
        while(index < length):
            slices.append(s[index:index+i])
            index = index+i
        # 현재 문자열과 다음 문자열이 동일하다면 압축 수(cnt) 증가   
        #                            동일하지 않다면 현재까지 결과 이어 붙이고 압축 수 초기화
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
