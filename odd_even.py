"""
Ask user for a number 
Print odd or even 
repeat till user quits
"""

def is_even(x):
    return x % 2 == 0 #return true if even 

print("Welcome to odd and even checker")
while True:
    #validate input 
    try:
        number = float(input("Enter a number"))
    except ValueError:
        print("Enter a value number")
        continue
    if is_even(number) is True:
        print("Even")
    else:
        print("Odd")
    choice = input("Type q to quit, else continue").lower()
    if choice.strip() == "q":
        print("Goodbye")
        break
    