import random
from math import gcd

"""
Generates large random 1024-bit number which is then passed to
function to test if its prime. Primality is tested with 
generated list of small primes first (sieve of Eratosthenes algortihm)
and then with rabin miller. Output is public- and private key
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
        p = self.generate_random_prime()
        q = self.generate_random_prime()

        while p == q:
            q = self.generate_random_prime()

        self.n = p * q

        t = (p - 1) * (q - 1)
        self.e = self.choose_e(t)
        self.d = self.modular_inverse(self.e, t)

        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def generate_random_prime(self):
        while True:
            prime = self.generate_random_number()
            if self.check_if_prime(prime):
                return prime

    def generate_random_number(self):
        large_number = random.getrandbits(1024)
        large_number |= 1 << 1023
        if large_number % 2 == 0:
            large_number += 1
        return large_number

    def check_if_prime(self, number):
        if number in self.small_primes:
            return True
        for prime in self.small_primes:
            if number % prime == 0:
                return False

        if not self.miller_rabin(number):
            return False

        return True

    def generate_small_primes(self):
        """
        generates 1229 primes
        """
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
        s = 0
        d = n
        while d % 2 == 0:
            s += 1
            d = d // 2
        return s, d

    def choose_e(self, t):
        e = 65537
        if gcd(e, t) == 1:
            return e
        while True:
            e = random.randrange(3, t, 2)
            if gcd(e, t) == 1:
                return e

    def extended_euclidean(self, a, b):  # de ≡ 1 (mod ϕ(n))
        if a == 0:
            return b, 0, 1
        greatest_common_divisor, x1, y1 = self.extended_euclidean(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return greatest_common_divisor, x, y

    def modular_inverse(self, e, t):
        greatest_common_divisor, x, y = self.extended_euclidean(e, t)
        if greatest_common_divisor == 1:
            return x % t
        return None


if __name__ == "__main__": #pragma: no cover
    k = KeyGenerator()
    primes = k.generate_small_primes()
    print(len(primes))
    print(k.generate_random_prime())
