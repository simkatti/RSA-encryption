import unittest
from unittest import mock
from encryption import Encryptor

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.e = Encryptor()
        self.message = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            "nostrud exercitation ullamco laboris"
        )
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
        with mock.patch.object(self.e.kg, 'get_public_key', return_value=((3233, 17))), \
            mock.patch.object(self.e.kg, 'get_private_key', return_value=((3233, 413))), \
                mock.patch.object(self.e.p, 'perform_padding', return_value=self.symbols_in_bytes):
            encypted, public_key, private_key = self.e.perform_encryption(
                self.symbols)
        expected = pow(self.symbols_int, 17, 3233)
        self.assertEqual(expected, encypted)
        self.assertEqual(public_key, (3233, 17))
        self.assertEqual(private_key, (3233, 413))

    def test_encyption_long_message(self):
        n = int('19130982778584820466324850465129434870651301035431612996773210'
                '93289172305915031110259373190713296732953569998144772835767169'
                '42174138727405095039065795656014960388855816890028766828437959'
                '50708634746400582494934267524510309580233869764553570680080124'
                '71795919339391486563216331240938087368884684065600546785479103'
                '46785320370484539465503199745520443626067998887718679634505439'
                '53447303219024623708456922345403948887008714005295309797801895'
                '06455108558239145176997018130429546202589349666736231437503751'
                '67834519462984326969282660557462562292789653965566895489530349'
                '27490047084282934315862848799242410248182306320827288929933'
        )
        e = 65537
        d = int('328458455871700565920147729425570900658511129973414268946842500'
                '292808135650944200263034120297023282103141273160580800891896033'
                '285534730116137354405653710343826280636228641317680753404019160'
                '739060632160999485787231923630931224791343196601579706519314778'
                '639309196835479337018159559262082101568047151034567194265238645'
                '549724720454197406840804650253518564672344209915052657560946712'
                '664312753946192633285911118211270148796124970968322347818800055'
                '219849601689139730579950331336681423319540618566013869895896695'
                '232463698506213747721886159366224861271219858726922654803449242'
                '6251598372686839555294578655587362755726392462513'
        )
        with mock.patch.object(self.e.kg, 'get_public_key', return_value=((n, e))), \
            mock.patch.object(self.e.kg, 'get_private_key', return_value=((n, d))), \
                mock.patch.object(self.e.p, 'perform_padding', return_value=self.msg_in_bytes):
            encypted, public_key, private_key = self.e.perform_encryption(
                self.message)
        expected_result = pow(self.msg_int, e, n)
        self.assertEqual(expected_result, encypted)
        self.assertEqual(public_key, (n, e))
        self.assertEqual(private_key, (n, d))
