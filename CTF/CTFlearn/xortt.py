sotr = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
pp = open("Examples/xoror", "w").write(sotr)
pop = "ctflearn{"
pip = "\x6a\x6f\x77\x6c\x73"
qqq = ""
for (i, p) in enumerate(sotr):
    # qqq = qqq + (p ^ pip[i % len(pip)])
    #print("%x" % ord(p))
    print("%x" % (ord(p) ^ ord(pop[i % len(pop)])))
    qqq += chr(ord(p) ^ ord(pip[i % len(pip)]))
print(qqq)
