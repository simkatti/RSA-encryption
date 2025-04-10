import unittest
from padding import Padder


class TestPadding(unittest.TestCase):
    def setUp(self):
        self.p = Padder()
        self.message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
        self.symbols = '!?=)&%€äöå023546'
        self.n = 16791873833114983445510379616427664045521811363064415229785683303523291226877353245881335625884701737379593219561805653887689977329954036172939095864460695127351360928905644629723155204218210777017023836077641067434925379320580781548946494483093339853623443133949716875345433414313046112649434644341278949173383963123674535605402464963186645670643671604023700206914964622408107266933023202872995628548503906342526880092254699185544781592935104121605640188321277623935978020096876284603472425176788617152167608644255036079580057053246714553018732562295776653349429294175651394885497384766197933488958320014767045491981 

        self.k = len(self.n.to_bytes((self.n.bit_length() + 7) // 8, "big")) 
        
        self.msg_in_bytes = self.message.encode('utf-8')
        self.msg_int = int.from_bytes(self.msg_in_bytes, 'big')

        self.symbols_in_bytes = self.symbols.encode('utf-8')
        self.symbols_int = int.from_bytes(self.symbols_in_bytes, 'big')   
             
    def test_padding_and_unpadding(self):
        padded_msg = self.p.perform_padding(self.n, self.message)
        unpadded_msg = self.p.reverse_padding(self.n, padded_msg)
        
        padded_symbols = self.p.perform_padding(self.n, self.symbols)
        unpadded_symbols= self.p.reverse_padding(self.n, padded_symbols)
        
        self.assertEqual(unpadded_msg, self.msg_in_bytes)
        self.assertEqual(unpadded_symbols, self.symbols_in_bytes)
        
    def test_message_length(self):
        mLen = self.k - 2 * 32 - 2 
        
        self.p.perform_padding(self.n, self.message)
        self.assertGreaterEqual(mLen, self.p.m_len)
        
        
    def test_mgf_with_invalid_length(self):
        l= 137438953475
        seed = b'\x00' * 32
        
        with self.assertRaises(ValueError):
            self.p.mask_generation_function(seed, l)
    
    def test_xor(self):
        a= b'\x01\x00'
        b= b'\x00\x10'
        expected = 272
        expected = expected.to_bytes((expected.bit_length() + 7) // 8, "big")
        
        result = self.p.xor(a,b)
        
        self.assertEqual(result, expected)
    
    def test_generate_padding_string(self):
        m_len = len(self.msg_in_bytes)
        h_len = 32
        ps_len =  self.k - m_len - 2 * h_len - 2
        result = self.p.generate_padding_string(self.k,m_len,h_len)
        
        self.assertEqual(len(result), ps_len)        
    
    def test_unsuccessful_padding(self):
        em = b'\x02\x88\x96%\xb7\xae.F9\x83\xe0\xbb\xa9h\xdfL\x80%yC\xa55\x8e\'J.8X](}\xa8\xae\xb2\xfd\x98\xa5\xb5\x90]\x9eb\xf3b\xee\xbcy"\x13\x7f\xff/\xc9\x9fh\xc4\x19+\xd6$Sy\x18\xea^l\rB\xa3\xb0W\xb6r\xbd];\xe3\xdb\x89UNu\xb3\xbaW\x8dV\xd4\xed\xc0\xdc\n\x8a\x99\xa0F\xfb\xdd\x19\x81@\xe9\xcd\xf5^Y\xbayQ/\x96B\xf4\xef\x04\xe2\xb1\x15\xb3`\x18j8\xf5\xfd\xe0\x96w\xc6\x89p\x12\x92\r\x9d\xad)q\xfe.\x1b\xd6u\x84\xd5\xe4\xd9\xf5\xbd\xed.P[s\xca\x15*\xb2\xba\xf9\x02\x1d\xed\xb2k+\xa29\x83A<\xe0\x0f\xd88\x19\xa45\x1b\x98l\x9cZs\x87\xc6\xdb\xfb\xc9\xc9\x03:\xe8]A\xb2@\xac\xbb\x19E\xdf\xa1H^\xaeo\xfa\xb8\x9f\x8e\xc8\x1d\xbfx\xc8\xb8\xc2\xb7\x89\xd5\x11c\xe7\x14\xfc\x16\x91\xa4\xfd\x9b\x0b]%F\x91;\xdf\xd9\x1a\x83Iv\x1c\x06\x0e\xdb\x7f\x17ht\x89\xebC\xb5\xcc'
        result = self.p.reverse_padding(self.n, em)
        
        self.assertEqual(result, None)