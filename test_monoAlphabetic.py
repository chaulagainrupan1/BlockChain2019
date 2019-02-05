from unittest import TestCase
from MonoAlphabetic import monoAlphabetic


class TestMonoAlphabetic(TestCase):
    def test_encryption(self):
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'HTKCUOISJYARGMZNBVFPXDLWQE'

        self.assertEqual(ciphertext, monoAlphabetic(plaintext,None).encryption())

    def test_decryption(self):
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'HTKCUOISJYARGMZNBVFPXDLWQE'

        self.assertEqual(plaintext, monoAlphabetic(None, ciphertext).decryption())
