# Foundation-of-CS-CW1
El Gamal algorithm implementation 
Description of the algorithm
First, the algorithm checks if the given number is prime; to generate the crypto graphic key .
Next, is to define the generate key function, which identifies the appropriate generator G for the multiplicative group of integers modulo p and generates a random prime number p.
After that, it computes the matching public key component y and creates a private key x
The encrypt function computes two ciphertext components  c1 and c2 , based on the public key and a randomly selected ephemeral key, to encrypt the plaintext integer that the user will input in  the program. Finally, the decrypt function extracts the original plaintext from the ciphertext using the private key. The application demonstrates how encryption and decryption work by printing out the generated public parameters, the encrypted message, and the decrypted message.
