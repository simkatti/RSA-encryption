<!-- Toteutusdokumentin tulee sisältää seuraavat:

Ohjelman yleisrakenne
Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)
Työn mahdolliset puutteet ja parannusehdotukset
Laajojen kielimallien (ChatGPT yms.) käyttö. Mainitse mitä mallia on käytetty ja miten. Mainitse myös mikäli et ole käyttänyt. Tämä on tärkeää!
Lähteet, joita olet käyttänyt, vain ne joilla oli merkitystä työn kannalta. -->

# Implementation

I'm interested in cyber security so I wanted to make a project related to cryptography. The process started with research: studying the algorithms and mathematics and planning the program structure. By the time I started coding and building the program, I had a clear idea how to implement it and where to start.

The program has three main components: graphical user interface (GUI), key generation and encryption and decryption.

### GUI

I started the project with coding the GUI first. The GUI allows user to input a message which length is 256 characters at maximum. This is the maximum size of 2048-bit key size encryption [[1]](https://mbed-tls.readthedocs.io/en/latest/kb/cryptography/rsa-encryption-maximum-data-size/).


### Key generation
Key generation is implemented in keygenerator.py. The file has methods for generating large 1024-bit numbers, generating a list of small prime numbers, Miller-Rabins test for primality and calculating the key components. 

The list of small prime numbers are calculated with the Sieve of Eratosthenes [[2]](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). I chose to generate 1000 first primes for better efficiency 

Miller-Rabins algorithm starts by factoring out the powers of two from the large prime candidate and then repeating modular exponentiation until requirement $n - 1 \equiv -1 \mod n$ is met. I chose k=100 because higher value of k gives higher accuracy weather the n is prime [[3]](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test).

The key components are calculated:
- $n = p \cdot q$
- $\lambda(n) = (p-1) \cdot (q-1)$
- $e = 65537$ as it is the most commonly chosen [[4]](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).
- d is computed by solving the equation $de \equiv 1(\mod \lambda(n))$ with Extended Euclidean Algorithm [[4]](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).


## Time and space complexity

## Potential improvements

## Use of AI
