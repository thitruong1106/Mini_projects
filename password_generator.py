import string, secrets, random

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Welcome to the Secure Password Generator!\n")

n_letters = int(input("How many letters? "))
n_symbols = int(input("How many symbols? "))
n_numbers = int(input("How many numbers? "))

password_list = []

for _ in range(n_letters):
    password_list.append(secrets.choice(letters))
for _ in range(n_symbols):
    password_list.append(secrets.choice(symbols))
for _ in range(n_numbers):
    password_list.append(secrets.choice(digits))

# Shuffle order securely
random.SystemRandom().shuffle(password_list)

password = "".join(password_list)
print("\nYour secure password is:", password)
