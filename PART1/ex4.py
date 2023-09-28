maximum_number = 10000


def isPerfect(value):
    cumsum = 0
    for i in range(1, value):    
        # Descubrir divisores
        if value%i == 0:
            cumsum += i
    if(cumsum == value):
        return True
    else:
        return False    
    
            

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()