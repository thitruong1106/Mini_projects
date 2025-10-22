#who pays the bill 
import random
friends = ["Richie", "Tee", "Nat", "steve", "sandy"]

print("The person paying the bill is " + random.choice(friends))

#loops 

"""
    for item in list_of_items:
        #do something each item 

"""

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

"""
Find higest score in list of scores 
"""

student_score = [12,20,40,10]

sum = 0

for score in student_score:
    sum+= score #add up each score 

print(sum)

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)

"""
Range 
for number in range(a,b)
    print(number)
"""

for n in range(0,10,2):
    print(n) #print 2,4,6,8