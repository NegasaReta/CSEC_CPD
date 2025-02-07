'''
If the letters are more uppercase, convert the string to uppercase.
If the letters are more lowercase, convert the string to lowercase.
If the number of uppercase and lowercase letters are the same, convert the string to lowercase.
'''
s = input()
upper = 0
lower = 0
for letter in s:
    if letter.isupper():
        upper+=1
    else:
        lower+=1
if upper>lower:
    s=s.upper()
else:
    s=s.lower()
print(s)
