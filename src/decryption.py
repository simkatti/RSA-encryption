"""encrypted message transformed back to ASCII
with private key"""

class Decryptor:
    def __init__(self):
        self.m = None

    def perform_decryption(self, c, private_key):
        n = private_key[0]
        d = private_key[1]
        m = pow(c, d, n)
        decrypted = self.int_to_text(m)
        return decrypted

    def int_to_text(self, m):
        msg_bytes = m.to_bytes((m.bit_length() + 7) // 8, "big")
        msg = msg_bytes.decode('utf-8')
        return msg
