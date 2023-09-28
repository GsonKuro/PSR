maximum_number = 50

#   Função para descubrir o número primo
def isPrime(value):
    for i in range(2,value):
        if value%i == 0:
           return False
    return True
            
# Função para indicar qual número é primo
def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()