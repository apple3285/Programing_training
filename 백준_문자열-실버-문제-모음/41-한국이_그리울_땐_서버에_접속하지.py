import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip().split("*")
start_p = pattern[0]
end_p = pattern[1]

for i in range(n):
    file = sys.stdin.readline().rstrip()
    if file.startswith(start_p) and file[len(start_p):].endswith(end_p):
        print("DA")
    else:
        print("NE")
