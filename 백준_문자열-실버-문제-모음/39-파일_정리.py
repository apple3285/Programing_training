#https://www.acmicpc.net/problem/20291
import sys

n = int(sys.stdin.readline())
dictionary = {}
for i in range(n):
    file = sys.stdin.readline()
    extension  = file.split(".")[1].rstrip()
    if extension in dictionary.keys():
        dictionary[extension]+=1
    else:
        dictionary[extension] = 1

dictionary = sorted(dictionary.items())

for extension, cnt in dictionary:
    print(extension, cnt)
