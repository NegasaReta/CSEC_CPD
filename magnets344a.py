n = int(input())
a = input()
sum = 1
 
for i in range(1, n):
    x = input()
    if x != a:
        sum += 1
        a = x
 
print(sum)
