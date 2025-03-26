## Week 3 report

### Hours used this week
28

### What I've done this week
This week I did unittest for keygenerator.py, modified GUI so that the keys are visible for the user and implimented decryption. Codecov coverage is also visible on readme!

### How the project has developed this week
Not much in terms of functionality but a lot in terms of testing

### What I learnt this week
How to impliments Mocks in unittests

### What challanges I faced this week
Not challenges per se but it's hard to know what to tests and how much and with which inputs.

Question: Are my tests ok? Should I do more or with different inputs? Performance tests? How? 
I will write the test report next week but I've tested:
- small primes are actually primes
- p and q values are 1024 bit each
- p and q are not the same value
- checking that rabin miller function works with known primes (true) and composites (false)
- modular inverse works (calculates correct answers)
- e as the common value if it passes the requirements (gcd(e,t) == 1) and if not it chooses another value for e
- generate_keys() function generates correct values for p, q, n, e and d 
- the key size (modulus n) is 2048 bits 

### What I will do next week
I continue doing tests: adding more for keygenerator.py if needed and start tests for encryption & decryption (quick because they only have two methods and its just the modular exponentiation). I will also start the testing documents and instructions for use for peer reviewing.
