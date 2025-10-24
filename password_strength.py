"""
    Purpose:
        Ask for a password 
        If length is < 8 (Weak)
        if contains digit + special characters = Strong
        else Moderate
"""
import string 
#Special character dict
sym = string.punctuation

password = input("Enter a password")

length = len(password) #check for length of password 
no_counter = 0 #check how many numbers in password 
sym_counter = 0 #check how many speical char are in this passowrd
for chr in password: #For each charcter in password 
    if chr.isdigit(): #if password is number 
        no_counter += 1 #Add one to number counter 
    elif chr in sym:
        sym_counter += 1
    else:
        continue

print(f"Your password is {length} this many charachter")
print(f"Your password contains {no_counter} this many digits")
print(f"Your password contains {sym_counter} this many symbol")

#Above works. Lets proceed for strenght checker 

#check the most specific condition first, 
if no_counter > 1 and sym_counter > 1 and length > 8: #if password contains 1 digit and 1 speical charcter and over 8 length 
    print("Strongest password")
elif length > 8 and no_counter > 1:
    print("Moderate pass")
elif length < 8:
    print("Weak password")