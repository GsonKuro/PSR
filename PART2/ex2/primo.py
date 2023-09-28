def isPrime(value):
    """
    Gets prime number
    value   : Evaluated number
    return  : Bool True or False
    """

    # If is a prime number then return true
    for i in range(2, value):
        if value%i == 0:
            return False
    return True