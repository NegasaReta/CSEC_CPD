n = int(input())
teams = []
for i in range(n):
    teams.append(list(map(int, input().split())))
    ans = 0
for i in range(n):
    for j in range(n):
        if teams[i][0] == teams[j][1]:
            ans += 1
print(ans)
