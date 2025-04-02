<!-- Testausdokumentin pitääs sisältää seuraavat:

Yksikkötestauksen kattavuusraportti.
Mitä on testattu, miten tämä tehtiin?
Minkälaisilla syötteillä testaus tehtiin?
Miten testit voidaan toistaa?
Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)
Ei siis riitä todeta, että testaus on tehty käyttäen automaattisia yksikkötestejä, vaan tarvitaan konkreettista tietoa testeistä, kuten:
Testattu, että tekoäly osaa tehdä oikeat siirrot tilanteessa, jossa on varma 4 siirron voitto. Todettu, että siirroille palautuu voittoarvo 100000.
Testattu 10 kertaan satunnaisesti valituilla lähtö- ja maalipisteillä, että JPS löytää saman pituisen reitin kuin Dijkstran algoritmi.
Kummallakin algoritmilla on pakattu 8 MB tekstitiedosto, purettu se ja tarkastettu, että tuloksena on täsmälleen alkuperäinen tiedosto. -->

# Test documentation

## Coverage report 
The program has three key modules: key generation, encryption and decryption. The code coverage for the key generation module is 98.96 % and 100 % for both encryption and decryption modules. There is one [line](https://app.codecov.io/gh/simkatti/RSA-encryption/blob/main/src%2Fkeygenerator.py#L113) in the key generation module that only has partial coverage. This happens because the statement on that line is always True, preventing the code from jumping back to the top of the `while True` loop. However, this does not affect the overall functionality of the algorithm.

The full coverage report can be found [here](https://app.codecov.io/gh/simkatti/RSA-encryption/tree/main/src)

## Unit testing
Unit tests are implimented separately for each module.  The key generation module contains the most methods and is the core of the program’s functionality, so most of the tests are focusing on that module. The key generation module consists methods of:
- generating small primes: returns a list of 1229 first small primes
- generating a random number: returns a random 1024-bit odd number
- generating a random prime: returns a random 1024-bit prime number if it passes the primality check. These are `p` and `q` values
- check if a number is a prime: uses the generated small prime list to check if a given number is divisible by any small primes. If not, the Miller-Rabin primality test is called. Returns True if the number is likely prime, otherwise False
- miller-rabin: factors out the powers of two from the large prime candidate and then repeats modular exponentiation until certain requirement is met. Returns True if prime candidate is likely to be a prime
- choosing public exponent `e`: returns commonly used value 65537 if it passes the requirements and if not, finds a new value for `e`

#### Generating small prime numbers
Key generation module has a method that generates 1229 first prime numbers. The method is tested by comparing its output to a list of the first 1000 known primes. The test passes if the first 1000 primes match. The generated list is also tested for primality using a separate method that checks each number by using the small prime list and the Miller-Rabin test. Since all tests pass, the method generates primes correctly.

### Generating random 1024-bit value
In 2048-bit RSA the modulus `n` should be 2048-bits. This means that `p` and `q` values should both be around 1024-bits. This is tested by checking that the method generating a random number returns a value of exactly 1024 bits in size. The method also ensures that if the generated number is even, 1 is added to it making it odd.  This is tested with a mock where the input`2**1023` is passed to the function and expected output is `2**1023 + 1`.

### Checking input for primality
This method combines two techniques for primality testing: checking divisibility with the small prime list values and performin Miller-Rabin test. 

Test inputs:
- a list of 10 randomly generated 1024-bit prime numbers. This list is generated and used by the program
- a list of 10 randomly generated 500-2000-bit prime numbers
- a list of composite numbers which are multiples of the 1024-bit primes
- a list of composites numbers which are multiples of the 500-2000-bit prime numbers

The tests pass if method returns True for all primes and false for all composites

### Miller Rabins test for primality
This method is tested with same inputs as the method above: two lists of randomly generated primes and their multiples as composites. Tests are passed if return value is asserted True for primes and False for composites.

### Choosing exponent e
The e is chosen so that `e < n ` and that `e` and `t` are coprime. The method is tested with two input: 17 and 131074. With 17 the method returns the common value 65537 because it meets the requirements. With 131074 the method searches another value for e since it doens't meet the requirements for the common value. The goal of this test is to test if the method finds another value for `e` if the requirements don't meet.

### Generating random prime
This method is tested using mock by giving the method return value of 1049 which is a known prime number. The method checks if its a prime and returns it. This test checks if a prime number is returned.

### Key values
The key values are tested with small input values that I calculated: `p = 3709 ,q = 7043, t = (p-1)*(q-1)//gcd(p-1,q-1), e = 65537, d = e**-1 * % t`. 
The test asserts correct with expected values. Other input values are large prime numbers generated by the program. The test is mocked to generate given `p` and `q` values. It's also tested that if the `p == q`. the method finds another value for `q`. This is tested with mocking the the `p` and `q` values to be 3709,3709,5861 and tested that the return value isn't a multiple of the same numbers.

### Key size
The modulus `n` size is tested to be 2048 +/- 1 bits to make sure it is the RSA 2048-bit standard. 
        
### Encryption and decryption

## Integration testing

## How to tests can be repeated
