from keygenerator import KeyGenerator


"""ascii message is transformed into large integer
which is then encrypted with modular exponentiation
and returned back to the GUI"""


class Encryptor:
    def __init__(self):
        self.m = None
        self.kg = KeyGenerator()

    def message_to_int(self, message):
        m_in_bytes = message.encode("utf-8")
        m = int.from_bytes(m_in_bytes, "big")
        return m

    def perform_encryption(self, message):
        self.m = self.message_to_int(message)
        self.kg.generate_keys()
        public_key = self.kg.get_public_key()
        private_key = self.kg.get_private_key()

        n = public_key[0]
        e = public_key[1]
        encrypted = pow(self.m, e, n)

        return encrypted, public_key, private_key
