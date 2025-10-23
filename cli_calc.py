
def mulitply(x,y):
    return x * y

def add(x,y):
    return x + y

def minus(x,y):
    return x - y 

def divide(x,y):
    return x / y

print("🧮 Welcome to the calculator Program")

while True:
    try:
        num_1 = float(input("Enter the first number"))
        num_2 = float(input("Enter the second number"))
    except ValueError:
        print("Please entry a valid number")
        continue
    op = input("What operation would you (*, +, -, /)").strip()
    if op == "/":
        if num_2 == 0:
            print("You cannot divide by zero")
        else:
            value = divide(num_1, num_2)
            print(f"{num_1} {op} {num_2} = {value}")
    elif op == "*":
        value = mulitply(num_1, num_2)
        print(f"{num_1} {op} {num_2} = {value}")
    elif op == "+":
        value = add(num_1, num_2)
        print(f"{num_1} {op} {num_2} = {value}")
    elif op == "-":
        value = minus(num_1, num_2)
        print(f"{num_1} {op} {num_2} = {value}")
    choice = input("Type q to quit, else type anything to continue").lower()
    if choice == "q":
        print("Goodbye")
        break