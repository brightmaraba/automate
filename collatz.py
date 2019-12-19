__author__ = "Brian Koech"
__author_email__ = "********"
__copyright__ = "Copyright (c) 2019 Libran Consult, Inc."
__license__ = "MIT"
def collatz(number):
    # Run if number is Even   
    if (number % 2 == 0):
        print (number // 2)
        return number // 2
    # Run this if number is Odd  
    else:
        print (number * 3 + 1)
        return number * 3 + 1
# Ensure user enters a number and call function recursively until n = 1
try:
    print("Enter a number")
    user_input = int(input(":> "))
except ValueError:
    print("Please enter a number")
else:
    while user_input != 1:
        user_input = collatz(int(user_input)) 
