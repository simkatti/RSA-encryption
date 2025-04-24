import unittest
from decryption import Decryptor
from encryption import Encryptor


class TestDecryption(unittest.TestCase):
    def setUp(self):
        self.d = Decryptor()
        self.e = Encryptor()
        self.message = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            "nostrud exercitation ullamco laboris"
        )
        self.symbols = '!?=)&%€äöå023546'

        msg_in_bytes = self.message.encode('utf-8')
        self.msg_int = int.from_bytes(msg_in_bytes, 'big')

        symbols_in_bytes = self.symbols.encode('utf-8')
        self.symbols_int = int.from_bytes(symbols_in_bytes, 'big')

    def test_decryption_message(self):
        c, pubkey, prikey = self.e.perform_encryption(self.message)
        n = prikey[0]
        d = prikey[1]
        decrypted = self.d.perform_decryption(c, prikey)
        self.assertEqual(decrypted, self.message)

    def test_decryption_symbols(self):
        c, pubkey, prikey = self.e.perform_encryption(self.symbols)
        n = prikey[0]
        d = prikey[1]
        decrypted = self.d.perform_decryption(c, prikey)
        self.assertEqual(decrypted, self.symbols)
