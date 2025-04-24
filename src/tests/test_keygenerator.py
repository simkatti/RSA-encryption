import unittest
from unittest import mock
from math import gcd
from keygenerator import KeyGenerator

class TestKeyGenerator(unittest.TestCase):

    def setUp(self):
        self.kg = KeyGenerator()

        self.small_primes = []
        with open('src/tests/known small primes.txt', encoding='utf-8') as file:
            for line in file:
                self.small_primes.append(int(line.strip('\n')))

        self.big_primes = []
        with open('src/tests/known large primes.txt', encoding='utf-8') as file:
            for line in file:
                self.big_primes.append(int(line.strip('\n')))

        self.big_composites = [self.big_primes[i] * self.big_primes[i + 1]
                               for i in range(0, len(self.big_primes) - 1, 2)]

    def test_generate_small_primes(self):
        generated_primes = self.kg.generate_small_primes()
        self.assertEqual(generated_primes[:1000], self.small_primes)

    def test_small_prime_list_for_primality(self):
        generated_primes = self.kg.generate_small_primes()
        for prime in generated_primes:
            self.assertTrue(self.kg.check_if_prime(prime))

    def test_generate_random_number_length(self):
        number = self.kg.generate_random_number()
        self.assertEqual(number.bit_length(), 1024)

    def test_generate_random_number_if_even(self):
        test_value = 2**1023
        with mock.patch('random.getrandbits', return_value=test_value):
            number = self.kg.generate_random_number()
        self.assertEqual(number, test_value+1)

    def test_check_if_prime(self):
        for prime in self.big_primes:
            self.assertTrue(self.kg.check_if_prime(prime))
        for composite in self.big_composites:
            self.assertFalse(self.kg.check_if_prime(composite))

    def test_miller_rabin(self):
        for prime in self.big_primes:
            self.assertTrue(self.kg.miller_rabin(prime))
        for composite in self.big_composites:
            self.assertFalse(self.kg.miller_rabin(composite))

    def test_choose_e(self):
        e = 65537
        self.assertEqual(self.kg.choose_e(17), e)
        self.assertNotEqual(self.kg.choose_e(131074), e)

    def test_generate_random_prime(self):
        small_prime = 1049
        with mock.patch.object(self.kg, 'generate_random_number', return_value=small_prime):
            number = self.kg.generate_random_prime()
        self.assertEqual(small_prime, number)

    def test_generate_keys(self):
        p = 3709
        q = 7043
        t = ((p-1)*(q-1))//gcd(p-1, q-1)
        e = 65537
        d = pow(e, -1, t)
        with mock.patch.object(self.kg, 'generate_random_prime', side_effect=[p, q]):
            self.kg.generate_keys()

        self.assertEqual(self.kg.n, p*q)
        self.assertEqual(self.kg.e, e)
        self.assertEqual(self.kg.d, d)
        self.assertEqual(self.kg.get_public_key(), (p*q, e))
        self.assertEqual(self.kg.get_private_key(), (p*q, d))

    def test_generate_key_large_values(self):
        p = self.big_primes[0]
        q = self.big_primes[3]
        t = ((p-1)*(q-1))//gcd(p-1, q-1)
        e = 65537
        d = pow(e, -1, t)

        with mock.patch.object(self.kg, 'generate_random_prime', side_effect=[p, q]):
            self.kg.generate_keys()

        self.assertEqual(self.kg.n, p*q)
        self.assertEqual(self.kg.e, e)
        self.assertEqual(self.kg.d, d)
        self.assertEqual(self.kg.get_public_key(), (p*q, e))
        self.assertEqual(self.kg.get_private_key(), (p*q, d))

    def test_same_p_q_values(self):
        p_q_values = iter([3709, 3709, 5861])
        with mock.patch.object(self.kg, 'generate_random_prime', side_effect=lambda: next(p_q_values)):
            self.kg.generate_keys()
        self.assertNotEqual(self.kg.n, 3709*3709)
        self.assertEqual(self.kg.n, 3709*5861)

    def test_modulus_size(self):
        self.kg.generate_keys()
        self.assertAlmostEqual(self.kg.n.bit_length(), 2048, delta=1)
