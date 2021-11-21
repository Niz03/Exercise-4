# Exercise 4 -  Light travels at 3 * 108 meters per second. A light-year is the distance a light beam travels in one year. Write a program that calculates and displays the value of a light-year.

# Declaration of Variables.
# Rate of the speed of light in m/s. The ** is the operator for exponent.
rate = 3 * 10 ** 8

# Seconds in a year.
seconds = 365 * 24 * 3600

# Basic multiplication.
distance = rate * seconds

# Final output
print("The value of a light year is " + str(distance) + " meters.")
