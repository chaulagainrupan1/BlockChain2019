class Vigenere:
    def __init__(self, plainText, cipheredText, key):
        self.plainText = plainText
        self.cipheredText = cipheredText
        self.key = key

    def encryption(self):
        plain = 'TOBEORNOTTOBE'
        key = 'RELATIONSRELA'
        ciphered = ''

        for i in self.plainText:
            if(ord(i) >= 97) and (ord(i) <= 122):
                   j = ord(i) - 97
                   k = ord(key[plain.index(i)]) - 97
                   if j+k > 25:
                       l = ((j+k) % 26)
                       l = l + 97
                       ciphered = ciphered + chr(l)
                   else:
                       l = j + k + 97
                       ciphered = ciphered + chr(l)

            elif(ord(i) >= 65) and (ord(i) <= 90):
                    j = ord(i) - 65
                    k = ord(key[plain.index(i)]) - 65
                    if j+k > 25:
                        l = ((j + k) % 26)
                        l = l + 65
                        ciphered = ciphered + chr(l)
                    else:
                        l = j + k + 65
                        ciphered = ciphered + chr(l)
        return ciphered

    def decryption(self):
        plaintext = ''
        key = 'RELATIONSRELA'
        ciphered = 'KSMESZBSKKSME'

        for i in self.cipheredText:
            if(ord(i) >= 97) and (ord(i) <= 122):
                j = ord(i) - 97
                k = ord(key[ciphered.index(i)]) - 97
                if j-k < 0:
                    l = (j-k) + 26 + 97
                    plaintext = plaintext + chr(l)
                else:
                    l = j-k + 97
                    plaintext = plaintext + chr(l)

            elif (ord(i) >= 65) and (ord(i) <= 90):
                j = ord(i) - 65
                k = ord(key[ciphered.index(i)]) - 65
                if j-k < 0:
                    l = (j-k) + 26 + 65
                    plaintext = plaintext + chr(l)
                else:
                    l = j-k + 65
                    plaintext = plaintext + chr(l)
        return plaintext

