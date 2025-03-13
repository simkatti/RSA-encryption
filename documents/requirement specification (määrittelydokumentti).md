## Requirement document
This is a course project for the "Algorithms and AI Lab" course in University of Helsinki's bachelor program in computer science. This project focuses on RSA encryption and decryption with the 2048 bit security standard. 

The RSA generates a public and private key using two large prime numbers which are found using Miller-Rabins algorithm. The message of ASCII characters are turned into integers which can be encrypted and decrypted with public and private key. 

This project is done with python and uses poetry as dependecy management. For peer-reviewing other projects I'd prefer python aswell. 

### Algorithms
**Miller-Rabin** algorithm to generate the two large prime numbers 

**Sieve of Eratosthenes** algorithm to pregenerate small prime numbers to help finding the large prime numberes

**Euclidean algorithm** to compute the *Carmichael's totient function* in key generation

**Modular exponentiation** for encryption and decryption

### Inputs
The user can input a message through user interface. The message can be maximum of 256 ASCII characters. The program will then encrypt the message and display is as an integer. The user can then decrypt the message back to letters. 

### Time complexity
Finding the large prime numbers is most expensive task of the program and its time complexity is O(k n³) where *k* is number of rounds performed for an *n*-digit number.

### References
[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

[Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

[Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function)

[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
