#문자열을 두 "균형잡힌 괄호 문자열" u, v로 분리하는 함수
def split_u_v(p):
    left = 0
    right = 0
    u = ""
    v = p
    for char in p:
        if char == "(":
            left += 1
        else :
            right += 1
        u += char
        v = v[1:]
        if left == right:
            break
    return(u,v)

def is_collect(u):
    stack =[]
    for char in u:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
    return True

def main(p):
    #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == "":
        return p
    else:
        #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        u,v = split_u_v(p)
        v_result= main(v)
        #3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        if is_collect(u):
            #3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
            return u + v_result
        #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        else :
            #4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            #4-3. ')'를 다시 붙입니다. 
            result = "" + "(" + v_result + ")"
            u = u[1:-1]
            u = u.replace("(","-")
            u = u.replace(")","(")
            u = u.replace("-",")")
            #4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            result += u
            #4-5. 생성된 문자열을 반환합니다.
            return result

def solution(p):
    answer = ''
    answer = main(p) 
    return answer
