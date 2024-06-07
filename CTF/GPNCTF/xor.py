import os

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+2],16)) for i in range(0,len(binaryString),2)])

#Задачча на crypto
def encrypt():
    key = "\x95\x1f\xae\x40\xc1"
    pz = "d24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d"
    message = toString(pz)
    print(message)
    out = ""
    for i in range(len(message)):
        #print("%x" % (ord(message[i])^ord(key[i%len(key)])))
        out+= chr(ord(message[i])^ord(key[i%len(key)]))
    return out
#key = os.urandom(5)

def encryptCr():
    pz = "4717591a4e08732410215579264e7e0956320367384171045b28187402316e1a7243300f501946325a6a1f7810643b0a7e21566257083c63043404603f5763563e43"
    message = toString(pz)
    print(message)
    out = message[0]
    for i in range(1, len(message)):
        #print("%x" % (ord(message[i])^ord(key[i%len(key)])))
        out+= chr(ord(message[i])^ord(message[i-1]))
    return out

print(encryptCr())