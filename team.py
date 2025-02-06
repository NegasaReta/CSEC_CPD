n = int (input())
 
result = 0
 
for _ in range (n):
    ls = list (map(int, input().rstrip().split()))
    p = ls[0]
    v = ls[1]
    t = ls[2]
    
    total = p+v+t
    if total>=2:
        result+=1
    else:
        continue
print(result)
