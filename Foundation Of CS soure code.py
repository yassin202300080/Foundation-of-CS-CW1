#By: Yassin Ahmed ElKholy 
import random
#check if number is prime
def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
#creating keys: public and private using random prime numbers
def generate_keys():
    #Finding random prime number
    while True:
        prime = random.randint(10, 100)
        if is_prime_number(prime):
            break

    #Finding suitable generator
    generator  = None
    for g in range(2 , prime):
        is_generator = True
        for q in range(2 , prime):
            if is_prime_number(q):
                if pow(g , (prime - 1) // q , prime) == 1:
                    is_generator = False
                    break
        if is_generator :
            generator = g
            break

    #Generating private key
    private_key = random.randint(1 , prime - 2)

    #The public key component calculation
    public_key_component = pow(generator, private_key, prime)

    return (prime , generator , public_key_component) , private_key