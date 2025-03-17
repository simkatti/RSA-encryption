import random 
from math import gcd

class KeyGenerator:
    
    def __init__(self):
        self. n = None
        self. e = None
        self.small_primes = self.generate_small_primes()
        self.d = None
        self.public_key = None
        self.private_key = None
        
    def generate_keys(self):
        p = self.generate_random_prime()
        q = self.generate_random_prime()
        while p == q:
            q = self.generate_random_prime()
            
        print(f"p:{p}")
        print(f"q:{q}")
        
        self.n = p * q
        t = (p-1)*(q-1)
        self.e = self.choose_e(t)
        
        print(f"n:{self.n}")
        print(f"t:{t}")
        print(f"e:{self.e}")
        # self.d
        
        self.public_key = (self.n,self.e)
        self.private_key = (self.n, self.d)
        
    def get_public_key(self):
        return self.public_key
    
    def get_private_key(self):
        return self.private_key
        
    def generate_random_prime(self):
        prime = 0
        while True:
            prime = self.generate_random_number()
            if self.check_if_prime(prime):
                return prime
        
    def generate_random_number(self):
        """p and q should both be 2048//2 size"""
        large_number = random.getrandbits(1024)
        if large_number % 2 == 0:
            large_number += 1
        return large_number
    
    def check_if_prime(self,number):
        for prime in self.small_primes:
            if number % prime == 0:
                return False
            
        # if not false do miller rabin
        
        return True
    
    def generate_small_primes(self):
        """sieve of Eratosthenes algortihm for small primes ranged 2 - 1009 """
        number_list = list(range(0,1010))
        number_list[0] = False
        number_list[1] = False
        for i in range(2,1010):
            if number_list[i] is not False:
                for j in range(i*i,1010, i):
                    number_list[j] = False
        small_primes = [number for number in number_list if number]
                
        return small_primes
    
    def miller_rabin(self):
        pass

    def choose_e(self, t): #optimise this or use 65537?
        for i in range(3,t,2):
            if gcd(i,t) == 1:
                return i
    


if __name__ == "__main__":
    k = KeyGenerator()
    k.generate_keys()
