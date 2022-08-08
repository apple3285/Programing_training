import sys

string = sys.stdin.readline().rstrip()+" "
# result = ""
# for word in s.split():
#     result += (word[::-1] + " ")
# result = result[:-1]
stack =[]
result =""
in_stack = False
temp=""
for s in string:
    if s == "<":
        if temp != "":
            result += temp[::-1]
            temp = ""
        
        stack.append(s)
        in_stack = True
    elif s == ">":
        stack.append(s)
        result+="".join(stack)
        stack=[]
        in_stack = False
    else:
        if in_stack:
            stack.append(s)
        else:
            if s == " ":
                result += temp[::-1]+ " "
                temp = ""
            else:
                temp += s
print(result.rstrip())
