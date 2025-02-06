limlak_weight, bob_weight = map(int, input().split())
numberofyears = 0
 
while (limlak_weight<=bob_weight):
    limlak_weight = limlak_weight*3
    bob_weight = bob_weight*2
    numberofyears = numberofyears + 1
    
print(numberofyears)
