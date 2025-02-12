def min_shovels(k, r):
    for n in range(1, 11):  # Checking up to 10 is sufficient
        if (n * k) % 10 == 0 or (n * k) % 10 == r:
            print(n)
            return

# Example usage
k, r = map(int, input().split())
min_shovels(k, r)
