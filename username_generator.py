import random, string 

symbols = string.punctuation #Get a list of symbols 
digits = string.digits #Get a list of digits 

print("Welcome to the username generator")

#Get user input 
name = input("Enter your name:").strip()
word = input("Enter your favourite word").strip()
birth = input("Enter your birth year").strip()

#Run program until user quits 
while True:
    #Creat username parts 
    username_part = [name,word,birth]
    username_part.append(random.choice(symbols)) #Add a random symbol to username 
    username_part.append(random.choice(digits)) #Add random number to username 

    #Shuffle the parts around 
    random.SystemRandom().shuffle(username_part)
    username = "".join(username_part) #Convert parts to one string 

    final_username = ""
    for char in username: #for each alpha letter in username, randomly convert to uppercose or lower and append it to final username
        final_username += char.upper()
    else:
        final_username += char.lower() 
    #Display username 
    print("\n The username generated for you is: ", final_username)

    #Ask for regneration 
    choice = input("\n Would you like to regenerate your username ? (y/n)").strip().lower() #Clean blank spaces and covert to lower letter 
    if choice in ("n", "no"): 
        print("Program ended")
        break #exit loop 
    