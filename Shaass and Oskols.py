def birds_on_wires(n, a, m, shots):
    for xi, yi in shots:
        xi -= 1  
        left_birds = yi - 1
        right_birds = a[xi] - yi
        
        if xi > 0:  
            a[xi - 1] += left_birds
        if xi < n - 1:  
            a[xi + 1] += right_birds
        
        a[xi] = 0  

    for birds in a:
        print(birds)

n = int(input().strip())
a = list(map(int, input().split()))
m = int(input().strip())
shots = [tuple(map(int, input().split())) for _ in range(m)]

birds_on_wires(n, a, m, shots)
