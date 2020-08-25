# Given the number of people in the room, calculate the probability that any two people in that room have the same birthday, 
# assuming we have 365 days in a year. (no leap years) 
# Return the probability rounded off to two decimal points.

import math
def calculate_probability(n):
    probability = 1- (math.factorial(365) / (math.factorial(365-n) * 365**n))
    return probability

print(round(calculate_probability(10), 2))
print(round(calculate_probability(20), 2))
print(round(calculate_probability(50), 2))
print(round(calculate_probability(100), 2))

# Alternative solution

def fact(x):
        a = 1
        for i in range(1, x+1):
            a *= i
        return a

def calculate_probability2(n):
    probability2 = 1- (fact(n) / (fact(365-n) * 365**n))
    return probability2

print(round(calculate_probability2(10), 2))
print(round(calculate_probability2(20), 2))
print(round(calculate_probability2(50), 2))
print(round(calculate_probability2(100), 2))