from keygenerator import KeyGenerator
from padding import Padder


"""ascii message is transformed into large integer
which is then encrypted with modular exponentiation
and returned back to the GUI"""


class Encryptor:
    def __init__(self):
        self.m = None
        self.kg = KeyGenerator()
        self.p = Padder()

    def message_to_int(self, message):
        return int.from_bytes(message, "big")

    def perform_encryption(self, message):
        self.kg.generate_keys()
        public_key = self.kg.get_public_key()
        private_key = self.kg.get_private_key()

        n = public_key[0]
        e = public_key[1]

        padded_message = self.p.perform_padding(n, message)
        self.m = self.message_to_int(padded_message)
        encrypted = pow(self.m, e, n)

        return encrypted, public_key, private_key
