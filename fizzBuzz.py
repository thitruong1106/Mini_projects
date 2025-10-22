for i in range(1,100+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0: 
        print("Fizz")
    else:
        print(i)


"""
Reflection: 
    i originally did if i % 3 == 0: but the first if statement should check for the most specific condition 
    Cause if n is both diviable by 3 and 5, it should print fizzbuzz, then check the rest.
"""