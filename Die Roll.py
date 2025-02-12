import math

def probability_of_dot_winning(Y, W):
    max_roll = max(Y, W)
    favorable_outcomes = 6 - max_roll + 1
    gcd = math.gcd(favorable_outcomes, 6) 
    print(f"{favorable_outcomes // gcd}/{6 // gcd}")

Y, W = map(int, input().split())
probability_of_dot_winning(Y, W)
