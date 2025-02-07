n1,n2,n3,n4 = map(int, input().split())
s = input()
calories = 0
for i in s:
    if i == '1':
        calories += n1
    elif i == '2':
        calories += n2
    elif i == '3':
        calories += n3
    else:
        calories += n4
print(calories)
