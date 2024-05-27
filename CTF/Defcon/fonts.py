from fontTools import ttLib


#tt = ttLib.TTFont("Quals2024.otf")
#tt.saveXML("1.xml")
tt1 = ttLib.TTFont("1.xml")
tt1.save("p.otf")
#magicNumber = tt['head'].magicNumber
#achVendID = tt['OS/2'].achVendID
#print(magicNumber, achVendID)
