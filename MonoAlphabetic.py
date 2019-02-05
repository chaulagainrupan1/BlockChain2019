class monoAlphabetic:
    def __init__(self, plainText, cipheredText):
        self.plainText = plainText
        self.cipheredText = cipheredText

    def encryption(self):
        ciphered = ''
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'HTKCUOISJYARGMZNBVFPXDLWQE'

        for i in self.plainText:
            ciphered = ciphered + ciphertext[plaintext.index(i)]
        return ciphered

    def decryption(self):
        plain = ''
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'HTKCUOISJYARGMZNBVFPXDLWQE'

        for i in self.cipheredText:
            plain = plain + plaintext[ciphertext.index(i)]
        print(plain)
        return plain
