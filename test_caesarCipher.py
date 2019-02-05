from unittest import TestCase
from caesarCipher import CaesarCipher


class TestCaesarCipher(TestCase):
    def test_encryption(self):
        plainText = "Home"
        cipheredText = "Jqog"

        self.assertEqual(cipheredText, CaesarCipher(plainText,None,2).encryption())

    def test_decryption(self):
        cipheredText = "Jqog"
        plainText = "Home"

        self.assertEqual(plainText, CaesarCipher(None, cipheredText,2).decryption())

if __name__ == 'main':
    TestCase.main()