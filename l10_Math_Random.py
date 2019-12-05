import math

# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))

import random

# Output: 16
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

#['d', 'c', 'b', 'e', 'a']
# Print the shuffled x
print(x)

# Print random element
print(random.random())


try:
	x = int(input("Enter a value :"))
	x= x+10
	print("X = " + str(x))
except :
    print("Please type an integer value !")


	