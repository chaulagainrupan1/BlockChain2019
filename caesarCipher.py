class CaesarCipher:
    def __init__(self, plainText, cipheredText, diff):
        self.plainText = plainText
        self.cipheredText = cipheredText
        self.diff = diff

    def encryption(self):
        cipheredText1 = ''
        for i in self.plainText:
            if(ord(i) >= 65) and (ord(i) <= 90):
                cipheredCharacter = ord(i) + self.diff
                if(cipheredCharacter)>90:
                    difference = value - 90
                    cipheredCharacter = 65 + difference

            elif (ord(i) >= 97) and (ord(i) <= 122):
                cipheredCharacter = ord(i) + self.diff
                if(cipheredCharacter) > 122:
                    difference = value - 122
                    cipheredCharacter = 97 + difference

            elif ord(i) == 32:
                cipheredCharacter = ord(i)

            cipheredText1 = cipheredText1 + chr(cipheredCharacter)
        return cipheredText1

    def decryption(self):
        plainText = ''
        for i in self.cipheredText:
            if(ord(i)>=65) and (ord(i)<= 90):
                plainCharacter = ord(i) - self.diff
            elif (ord(i) >= 97) and (ord(i)<= 122):
                plainCharacter = ord(i) - self.diff
            elif ord(i) == 32:
                plainCharacter = ord(i)
            plainText = plainText + chr(plainCharacter)
        return plainText

