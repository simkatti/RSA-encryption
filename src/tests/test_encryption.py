import unittest
from encryption import Encryptor
from unittest import mock


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.e = Encryptor()
        self.message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
        self.symbols = '!?=)&%€äöå023546'

        self.msg_in_bytes = self.message.encode('utf-8')
        self.msg_int = int.from_bytes(self.msg_in_bytes, 'big')

        self.symbols_in_bytes = self.symbols.encode('utf-8')
        self.symbols_int = int.from_bytes(self.symbols_in_bytes, 'big')

    def test_message_to_int(self):
        result = self.e.message_to_int(self.symbols_in_bytes)
        self.assertEqual(self.symbols_int, result)

    def test_long_message(self):
        result = self.e.message_to_int(self.msg_in_bytes)
        self.assertEqual(self.msg_int, result)

    def test_encyption(self):
        with mock.patch.object(self.e.kg, 'get_public_key', return_value=((3233, 17))), mock.patch.object(self.e.kg, 'get_private_key', return_value=((3233, 413))), \
                mock.patch.object(self.e.p, 'perform_padding', return_value=self.symbols_in_bytes):
            encypted, public_key, private_key = self.e.perform_encryption(
                self.symbols)
        expected = pow(self.symbols_int, 17, 3233)
        self.assertEqual(expected, encypted)
        self.assertEqual(public_key, (3233, 17))
        self.assertEqual(private_key, (3233, 413))

    def test_encyption_long_message(self):
        n = 19130982778584820466324850465129434870651301035431612996773210932891723059150311102593731907132967329535699981447728357671694217413872740509503906579565601496038885581689002876682843795950708634746400582494934267524510309580233869764553570680080124717959193393914865632163312409380873688846840656005467854791034678532037048453946550319974552044362606799888771867963450543953447303219024623708456922345403948887008714005295309797801895064551085582391451769970181304295462025893496667362314375037516783451946298432696928266055746256229278965396556689548953034927490047084282934315862848799242410248182306320827288929933
        e = 65537
        d = 3284584558717005659201477294255709006585111299734142689468425002928081356509442002630341202970232821031412731605808008918960332855347301161373544056537103438262806362286413176807534040191607390606321609994857872319236309312247913431966015797065193147786393091968354793370181595592620821015680471510345671942652386455497247204541974068408046502535185646723442099150526575609467126643127539461926332859111182112701487961249709683223478188000552198496016891397305799503313366814233195406185660138698958966952324636985062137477218861593662248612712198587269226548034492426251598372686839555294578655587362755726392462513
        with mock.patch.object(self.e.kg, 'get_public_key', return_value=((n, e))), mock.patch.object(self.e.kg, 'get_private_key', return_value=((n, d))), \
                mock.patch.object(self.e.p, 'perform_padding', return_value=self.msg_in_bytes):
            encypted, public_key, private_key = self.e.perform_encryption(
                self.message)
        expected_result = pow(self.msg_int, e, n)
        self.assertEqual(expected_result, encypted)
        self.assertEqual(public_key, (n, e))
        self.assertEqual(private_key, (n, d))
