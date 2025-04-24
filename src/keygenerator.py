import random
from math import gcd

"""
Generates and outputs public- and private key.

"""


class KeyGenerator:

    def __init__(self):
        self.n = None
        self.e = None
        self.small_primes = self.generate_small_primes()
        self.d = None
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """Generates the key components"""
        p = self.generate_random_prime()
        q = self.generate_random_prime()

        while p == q:
            q = self.generate_random_prime()

        self.n = p * q

        t = ((p - 1) * (q - 1)) // gcd((p-1), (q-1))
        self.e = self.choose_e(t)
        self.d = pow(self.e, -1, t)

        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def generate_random_number(self):
        """Generates random 1024-bit number"""
        large_number = random.getrandbits(1024)
        large_number |= 1 << 1023
        if large_number % 2 == 0:
            large_number += 1
        return large_number

    def generate_random_prime(self):
        """Checks if randomly generated number is prime"""
        while True:
            prime = self.generate_random_number()
            if self.check_if_prime(prime):
                return prime

    def check_if_prime(self, number):
        """The primality is tested first with small prime list
        and then with rabin millers algorithm. 
        Returns true if number likely to be prime"""
        if number in self.small_primes:
            return True
        for prime in self.small_primes:
            if number % prime == 0:
                return False

        if not self.miller_rabin(number):
            return False

        return True

    def generate_small_primes(self):
        """Generates 1229 first primes with Sieve of Eratosthenes algorithm"""
        number_list = list(range(0, 10000))
        number_list[0] = False
        number_list[1] = False
        for i in range(2, 10000):
            if number_list[i] is not False:
                for j in range(i * i, 10000, i):
                    number_list[j] = False
        small_primes = [number for number in number_list if number]

        return small_primes

    def miller_rabin(self, n):
        """Miller-Rabins test for primality. Returns true if modular exponentation meets requirements k times"""
        s, d = self.factor_out_powers_of_two(n - 1)
        for _ in range(100):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x in (1, n - 1):
                continue
            for _ in range(s):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def factor_out_powers_of_two(self, n):
        """Outputs values s and n. 
        s is how many times the number 2 is factor of n 
        and d is n with all factors of 2 removed  """
        s = 0
        d = n
        while d % 2 == 0:
            s += 1
            d = d // 2
        return s, d

    def choose_e(self, t):
        """Primarily uses the common value for e if requirements are met otherwise e is computed """
        e = 65537
        if gcd(e, t) == 1:
            return e
        while True:
            e = random.randrange(3, t, 2)
            if gcd(e, t) == 1:
                return e
