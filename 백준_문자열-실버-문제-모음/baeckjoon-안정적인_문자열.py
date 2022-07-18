import sys
def check_stable(string):
    string = list(string)
    stack= []
    unstable_string=[]
    for now in string:
        if now =="{":
            stack.append(now)
        elif now == "}":
            if not stack or stack[-1] != "{":
                unstable_string.append(now)
        

for line in sys.stdin:
    if "-" in line:
        break
    string = line.rstrip()
    check_stable(string)

