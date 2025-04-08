"""Not sure if I will impliment this"""
#https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding
#hash function SHA-256 for 2048 RSA

from hashlib import sha256 
import random

class Padder:
    def __init__(self):
        pass
    
    def perform_padding(self,n,m): #message must be up most k-mLen - 2 *hLen-2 bytes!! --> 190 characteres? 
        lHash = self.hash_function()
        ps = self.generate_padding_string(n,m,lHash)
        datablock = lHash + ps + b'\x01' + m.encode('utf-8')
        seed = self.generate_seed(len(lHash))
        dbMask = self.mask_generating_function(seed, (len(n.encode('utf-8')) - len(lHash) - 1))
        maskedDB = self.xor(datablock, dbMask)
        seedMask = self.mask_generating_function(maskedDB,len(lHash))
        maskedSeed = self.xor(seed, seedMask)
        
        return  b'\x00' + maskedSeed + maskedDB
    
    def mask_generating_function(self, a, b): #dbMask = MGF(seed, k-hLen-1)
        pass
    
    def hash_function(self):
        lHash = sha256(''.encode('utf-8')).digest()
        return lHash
    
    def xor(self, a,b):
        pass
    
    def generate_padding_string(self,n,m,h): #k-mLen - 2 *hLen-2
        k = len(n.encode('utf-8'))
        mLen = len(m.encode('utf-8'))
        hLen = len(h)
        bytecount = k - mLen - 2 * hLen - 2
        return b'\x00' * bytecount
    
    def generate_seed(length):
        return [random.randint(0, 255) for _ in range(length)]
    
    def reverse_padding(self, n, em): 
        lHash = self.hash_function()
        _, maskedSeed, maskedDB = em[0], em[1], em[2] #split encoded message EM into 0x00, maskedSeed length of hLen AND maskedDb
        seedMask = self.mask_generating_function(maskedDB, len(lHash))
        seed = self.xor(maskedSeed, seedMask)
        dbMask = self.mask_generating_function(seed, len(n.encode('utf-8')) - len(lHash) -1) # k is len(bytes(n)))
        datablock = self.xor(maskedDB, dbMask)
        lhash, ps, b'\x01', m = datablock[0], datablock[1], datablock[2], datablock[3] #lhas == lHash, ps is only of 0x00's, ps and m are separated by 0x01 byte, the first byte of EM is 0x00
        return m
    
if __name__ == "__main__": 
    p = Padder()
    print(p.hash_function())