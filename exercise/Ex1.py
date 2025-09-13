# Q1.# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
Color = "Blue"

# ❓ Question Statement:

# Q2.
# We are working with a circle that has a diameter of 3.

# Create a variable called radius equal to half the diameter.

# Create a variable called area, using the formula for the area of a circle:Area=π×r2
pi = 3.14159  
diameter = 3
 
radius = diameter/2

# area = pi*radius^2
area = pi*(radius**2)
print(area)


# Q3.# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
#   Swap the values to which a and b refer
temp = a
a = b
b = temp

# Q4.Add parentheses to the following expression so that it evaluates to 0.
8 - 3 * 2 - 1+ 1

# Q5.Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash =  (121 + 77 + 109) % 3