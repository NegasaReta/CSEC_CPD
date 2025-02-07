s = input()
letters = 'abcdefghijklmnopqrstuvwxyz'
pos = 0
rotations = 0
for i in s:
    index = letters.index(i)
    rotations += min(abs(index - pos), 26 - abs(index - pos))
    pos = index
print(rotations)
