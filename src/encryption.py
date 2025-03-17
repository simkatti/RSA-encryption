from keygenerator import KeyGenerator

class Encryptor:
    
    def __init__(self):
        self.m = None
        self.kg = KeyGenerator()
    
    def message_to_int(self, message="Hello!"):
        m_in_bytes = message.encode("utf-8")
        m = int.from_bytes(m_in_bytes, "big")
        return m
    
    def perform_encryption(self, message="Hello"):
        print(message)
        self.m = self.message_to_int(message)
        print(self.m)
        self.kg.generate_keys()
        public_key = self.kg.get_public_key()
        
        n = public_key[0]
        print(f"n:{n}")
        e = public_key[1]
        print(f"e:{e}")
        
        encrypted = (self.m**e)% n
        
        print(f"encrypted msg: {encrypted}")
        
        return encrypted
        
if __name__ == "__main__":
    e = Encryptor()
    e.perform_encryption()