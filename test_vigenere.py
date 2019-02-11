from unittest import TestCase
from Vigenere import Vigenere


class TestVigenere(TestCase):
    def test_encryption(self):
        plainText = 'TOBEORNOTTOBE'
        key = 'RELATIONSRELA'
        cipheredText = 'KSMEHZBBLKSME'

        self.assertEqual(cipheredText, Vigenere(plainText, None, key).encryption())


    def test_decryption(self):
        plainText = 'TOBEORNOTTOBE'
        key = 'RELATIONSRELA'
        cipheredText = 'KSMEHZBBLKSME'

        self.assertEqual(plainText, Vigenere(None, cipheredText, key).decryption())
