"""
    Pick a random number between 1-10 
    ask user to guess until they are corerct
    print number of attempt 
"""
import random 

count = 0
random_no = random.randint(1,10) #get a random number 1 - 10
while True: 
    #validate input
    try:
        guess = int(input("Guess the number"))
    except ValueError:
        print("Please enter a valid number")
        continue
    if guess != random_no: #if guess is wrong 
        print("Try again")
        count += 1 #add one to counter 
    elif guess == random_no: #guess is correct 
        print(f"You attempt {count} times")
        print(f"The number picked randomly was {random_no}")
        break
