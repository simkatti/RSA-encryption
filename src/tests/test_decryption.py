import unittest
from decryption import Decryptor
from encryption import Encryptor

class TestDecryption(unittest.TestCase):
    def setUp(self):
        self.d = Decryptor()
        self.e = Encryptor()
        self.message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in'
        self.symbols = '!?=)&%€äöå023546'
        
    def test_int_to_text(self):
        m_in_bytes = self.message.encode("utf-8")
        m = int.from_bytes(m_in_bytes, "big")
        s_in_bytes = self.symbols.encode("utf-8")
        s = int.from_bytes(s_in_bytes, "big")
        message = self.d.int_to_text(m)
        symbols = self.d.int_to_text(s)
        
        self.assertEqual(message, self.message)
        self.assertEqual(symbols, self.symbols)
    
    def tetst_decryption(self):
        c, pubkey, prikey = self.e.perform_encryption(self.message)
        n = prikey[0]
        d = prikey[1]
        m = pow(c,d,n)
        encrypted = self.d.perform_decryption(c,prikey)
        self.assertEqual(encrypted,self.message)
    
    def test_decryption_symbols(self):
        c, pubkey, prikey = self.e.perform_encryption(self.symbols)
        n = prikey[0]
        d = prikey[1]
        m = pow(c,d,n)
        encrypted = self.d.perform_decryption(c,prikey)
        self.assertEqual(encrypted,self.symbols)