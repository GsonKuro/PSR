#!/usr/bin/env python3

maximum_number = 100

# Fuctions to get dividers of number
def getDivider(value):
    """
    Gets a list of integer dividers of number value
    value   : Number to get dividers
    return  : List of deviders
    """

    # List of dividers
    dividers = []

    # List all dividers
    for i in range(1, value):
        if value%i == 0:
            dividers.append(i)
    
    # Returns list of dividers
    return dividers

# Function to get perfect number
def isPerfect(value):
    """
    Sums the list of dividers of the value to evaluate if is a perfect number
    value   : Number to check if is perfect
    return  : Bool true or false
    """
    # Create variable of type getDivider and the fucntion
    dividers = getDivider(value)

    # Returns if the sum of list of dividers is equal to the value
    return value == sum(dividers)

def main():
    """
    Runs main code

    """

    print("Starting to compute perfect numbers up to " + str(maximum_number))

    #  Runs throught all number to check if is a perfect number
    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
