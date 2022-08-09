#https://www.acmicpc.net/problem/1302
import sys

n = int(sys.stdin.readline())
books = {}
for i in range(n):
    book = sys.stdin.readline().rstrip()
    if  book in books.keys():
        books[book] += 1
    else:
        books[book] = 1
sort_books = sorted(books.items(), key=lambda x:(-x[1],x[0]))
print(sort_books[0][0])
