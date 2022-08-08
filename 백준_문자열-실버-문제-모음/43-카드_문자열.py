import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    cards = sys.stdin.readline().rstrip().split()
    result =""
    before_ascii = 1000
    for card in cards:
        if before_ascii >= ord(card):
            result = card+result
            before_ascii = ord(card)
        else:
            result = result+card
    print(result)
