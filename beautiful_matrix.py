matrix = [[],[],[],[],[]]
location_of_1  = []
 
for i in range (5):
    row = list(map(int, input().rstrip().split()))
    matrix[i]=row
    
for i in range (5):
    for j in range(5):
        if matrix[i][j] == 1:
            location_of_1 = [i,j]
            
midval_x = 2
midval_y = 2
 
answer = abs(location_of_1[0]-midval_x)+abs(location_of_1[1]-midval_y)
print (answer)
