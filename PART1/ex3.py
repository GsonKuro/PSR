
maximum_number = 50

def isPrime(value):
    for i in range(2,value):
        if value%i == 0:
            print(str(value) + " e divisivel por " + str(i))
            return False
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()