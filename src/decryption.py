from padding import Padder

"""encrypted message transformed back to ASCII
with private key"""

class Decryptor:
    def __init__(self):
        self.m = None
        self.p = Padder()

    def perform_decryption(self, c, private_key):
        n = private_key[0]
        d = private_key[1]
        m = pow(c, d, n)
        k = len(n.to_bytes((n.bit_length() + 7) // 8, "big"))
        msg_bytes = m.to_bytes((m.bit_length() + 7) //
                               8, "big").rjust(k, b'\x00')
        unpadded_msg = self.p.reverse_padding(n, msg_bytes)

        decrypted = unpadded_msg.decode('utf-8')
        return decrypted
