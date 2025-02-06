string = input ()
#convert the characters in the string  to a list of characters
 
slist = list (string)
 
#convert the list to a set to remove the duplicates
username = set(slist)
 
if len (username)%2==0:
    print ("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
