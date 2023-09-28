def isPrime(value):
    """
    Gets prime number
    value   : Evaluated number
    return  : Bool True or False
    """

    limit = round((value/2)+1)

    # If is a prime number then return true
    for i in range(2, limit):
        if value%i == 0:
            return False
    return True