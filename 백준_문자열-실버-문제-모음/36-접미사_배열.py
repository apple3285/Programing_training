import sys
S = sys.stdin.readline().rstrip()
suffix_list =  sorted([S[i:] for i in range(len(S))])
for suffix in suffix_list:
    print(suffix)
