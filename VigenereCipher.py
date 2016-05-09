#!/bash/python

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, message):
        j = 0
        newMess = []
        for i in range(0, len(message)):
            if j >= len(self.key):
                j = 0
            if message[i] in self.alphabet:
                newMess.append(convertChar(message[i], self.key[j], self.alphabet, True))
                j+=1
            else:
                newMess.append(message[i])
                j += 1
        return "".join(newMess)


    def decode(self, message):
        j = 0
        newMess = []
        for i in range(0, len(message)):
            if j >= len(self.key):
                j = 0

            if message[i] in self.alphabet:
                newMess.append(convertChar(message[i], self.key[j], self.alphabet, False))
                j+=1
            else:
                newMess.append(message[i])

        return "".join(newMess)

def convertChar(mess, key, alphabet, encode):
    indexM = alphabet.index(mess)
    indexK = alphabet.index(key)

    if(encode):
        return alphabet[(indexM + indexK) % 26]
    else:
        return alphabet[(indexM - indexK) % 26]


##main function test

cipher = VigenereCipher("password", "abcdefghijklmnopqrstuvwxyz")

print cipher.encode("it's a shift cipher")
