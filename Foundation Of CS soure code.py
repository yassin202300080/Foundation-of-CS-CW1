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
    try:
        #Finding random prime number
        while True:
            prime = random.randint(100, 100*10)
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

        return (prime, generator, public_key_component), private_key

    except Exception as e:
        print(f"No Suitable Generator Found: {e}")

#Encrypt the plaintext message
def encrypt(crypto_key , plaintext):
    prime , generator , public_key_component = crypto_key
    #Encrypting function
    plaintext = plaintext % prime
 #choosing random ephemeral key
    ephemeral_key = random.randint(1 , prime - 2) 
    c1 = pow(generator , ephemeral_key , prime)  
    c2 = (plaintext * pow(public_key_component, ephemeral_key, prime)) % prime  
    return c1, c2  
#decrypting  the plaintext message
def decrypt(private_key, crypto_key, ciphertext):
    prime, _, _ = crypto_key
    c1, c2 = ciphertext
    shared_secret = pow(c1, private_key, prime) 
    shared_secret_inverse = pow(shared_secret, prime - 2, prime)  
    return (c2 * shared_secret_inverse) % prime 

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    print(f"Public parameters: prime Number = {public_key[0]}, Generator = {public_key[1]}")
    print(f" secret Private key: x = {private_key}")

    #Error handling: Ensure the plaintext input from user is less than the prime number
    prime = public_key[0]
    while True:
        try:
            plaintext = int(input(f"enter an integer to encrypt (Integer must be less than {prime}): "))
            if plaintext >= prime:
                raise ValueError(f"Input must be less than {prime}.")
            break
        except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")

    ciphertext = encrypt(public_key, plaintext)
    print(f"Encrypted message: ciphertext 1 = {ciphertext[0]}, ciphertext2 = {ciphertext[1]}")

    decrypted_message = decrypt(private_key, public_key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")