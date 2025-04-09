import pytest
from encryption import Encryptor
from decryption import Decryptor


class TestIntegration:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.e = Encryptor()
        self.d = Decryptor()
        self.long_msg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
        self.symbols = '!?=)&%€äöå023546'
        self.msg = 'Hello World!'

    def test_integration_long_message(self):
        encrypted_msg, public_key, private_key = self.e.perform_encryption(
            self.long_msg)
        decrypted = self.d.perform_decryption(encrypted_msg, private_key)

        assert decrypted == self.long_msg

    def test_integration_symbols(self):
        encrypted_msg, public_key, private_key = self.e.perform_encryption(
            self.symbols)
        decrypted = self.d.perform_decryption(encrypted_msg, private_key)

        assert decrypted == self.symbols

    def test_integration_message(self):
        encrypted_msg, public_key, private_key = self.e.perform_encryption(
            self.msg)
        decrypted = self.d.perform_decryption(encrypted_msg, private_key)

        assert decrypted == self.msg
