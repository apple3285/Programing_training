import sys
T = int(sys.stdin.readline())

for i in range(T):
    record = " "+sys.stdin.readline()
    sounds =[]
    for line in sys.stdin:
        line = line.rstrip()
        if line == "what does the fox say?":
            break
        sound = line.split("goes")[1]
        record = record.replace(sound,"")
    print(record.strip())
