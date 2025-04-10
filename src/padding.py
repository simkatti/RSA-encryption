from hashlib import sha256
import random

"""Handles padding for messages to be encrypted and unpadding for decryption.
The padding is done with mask generation function and SHA-256 hash function"""

class Padder:
    def __init__(self):
        self.lhash = self.hash_function(b'')
        self.lhash_len = len(self.lhash)
        self.k = None
        self.m_len = None

    def perform_padding(self, n, m):
        self.k = len(n.to_bytes((n.bit_length() + 7) // 8, "big"))
        self.m_len = len(m.encode('utf-8'))
        ps = self.generate_padding_string(self.k, self.m_len, self.lhash_len)
        datablock = self.lhash + ps + b'\x01' + m.encode('utf-8')
        seed = self.generate_seed(self.lhash_len)
        db_mask = self.mask_generation_function(seed, self.k - self.lhash_len - 1)
        masked_db = self.xor(datablock, db_mask)
        seed_mask = self.mask_generation_function(masked_db, self.lhash_len)
        masked_seed = self.xor(seed, seed_mask)

        return b'\x00' + masked_seed + masked_db

    def mask_generation_function(self, seed, l):
        if l > (self.lhash_len << 32):
            raise ValueError('Mask too long')

        t = b''
        counter = 0
        while len(t) < l:
            c = counter.to_bytes(4, 'big')
            t += self.hash_function(seed + c)
            counter += 1

        return t[:l]

    def hash_function(self, hash_value):
        return sha256(hash_value).digest()

    def xor(self, a, b):
        int_a = int.from_bytes(a, 'big')
        int_b = int.from_bytes(b, 'big')
        xor_result = int_a ^ int_b
        return xor_result.to_bytes((xor_result.bit_length() + 7) // 8, "big")

    def generate_padding_string(self, k, m_len, h_len):
        bytecount = k - m_len - 2 * h_len - 2
        return b'\x00' * bytecount

    def generate_seed(self, length):
        """A single byte (8-bits) can represent 256 numbers"""
        return bytes(random.randint(0, 255) for _ in range(length))

    def split_datablock(self, datablock):
        lhash = datablock[:self.lhash_len]
        sliced_db = datablock[self.lhash_len:]
        separating_byte = sliced_db.index(b'\x01')
        ps = sliced_db[:separating_byte]
        m = sliced_db[separating_byte + 1:]

        return lhash, ps, m

    def reverse_padding(self, n, em):
        self.k = len(n.to_bytes((n.bit_length() + 7) // 8, "big"))
        null_byte, masked_seed, masked_db = em[0:1], em[1:self.lhash_len +1], em[self.lhash_len + 1:]
        seed_mask = self.mask_generation_function(masked_db, self.lhash_len)
        seed = self.xor(masked_seed, seed_mask)
        db_mask = self.mask_generation_function(seed, self.k - self.lhash_len - 1)
        datablock = self.xor(masked_db, db_mask)
        lhash, ps, m = self.split_datablock(datablock)

        """verify that padding is successfull"""
        if lhash == self.lhash and ps == b'\x00' * len(ps) and \
            datablock[self.lhash_len:] == ps + b'\x01' + m and em[0] == 0x00:
            return m

        return None
