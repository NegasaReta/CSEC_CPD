def final_position(s, t):
    position = 0 
    for instruction in t:
        if s[position] == instruction:
            position += 1  

    print(position + 1)  

s = input().strip()
t = input().strip()
final_position(s, t)
