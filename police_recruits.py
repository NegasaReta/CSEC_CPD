n = int (input())
event = list(map(int, input().split()))

police = 0
untreated = 0
for i in range (n):
    if event[i] == -1:
        if police == 0:
            untreated += 1
        else:
            police -= 1
    else:
        police += event[i]
print (untreated)
