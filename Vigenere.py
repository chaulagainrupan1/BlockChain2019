class Vigenere:
    def __init__(self, plainText, cipheredText, key):
        self.plainText = plainText
        self.cipheredText = cipheredText
        self.key = key

    def encryption(self):
        plain = 'TOBEORNOTTOBE'
        key = 'RELATIONSRELA'
        ciphered = ''
        b = 0
        for i in self.plainText:
            a = len(key)
            if(ord(i) >= 97) and (ord(i) <= 122):
                    j = ord(i) - 97
                    k = ord(key[b]) - 97
                    l = ((j+k) % 26) + 97
                    ciphered = ciphered + chr(l)
                    b = b + 1

            elif(ord(i) >= 65) and (ord(i) <= 90 and b <= a):
                    j = ord(i) - 65
                    k = ord(key[b]) - 65
                    l = ((j + k) % 26) + 65
                    ciphered = ciphered + chr(l)
                    b = b + 1
                    print(b)
        return ciphered

    def decryption(self):
        plaintext = ''
        key = 'RELATIONSRELA'
        ciphered = 'KSMEHZBBLKSME'
        b = 0
        for i in self.cipheredText:
            a = len(key)
            if(ord(i) >= 97) and (ord(i) <= 122) and (b < a):
                j = ord(i) - 97
                k = ord(key[b]) - 97
                if j-k < 0:
                    l = (j-k) + 26 + 97
                    plaintext = plaintext + chr(l)
                else:
                    l = j-k + 97
                    plaintext = plaintext + chr(l)
                b = b + 1


            elif(ord(i) >= 65) and (ord(i) <= 90) and (b < a):
                j = ord(i) - 65
                k = ord(key[b]) - 65
                if j-k < 0:
                    l = (j-k) + 26 + 65
                    plaintext = plaintext + chr(l)
                else:
                    l = j-k + 65
                    plaintext = plaintext + chr(l)
                b = b + 1
        return plaintext

