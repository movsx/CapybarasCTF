# Преобразовать бинари строку в ASCII (строка должна быть без пробелов)
def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

# Преобразовать каждый символ в бинари строку
def toBinary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])

# Пример решения задачи на быструю проверку LSB флага
# Что такое LSB? Это когда в младшие байты запихивают полезную информацию сразу в ASCII
def LSB_Check():
    from PIL import Image
    img = Image.open("Examples/stego.png")
    red, green, blue, alpha = img.split()
    width, height = img.size

    r_lsb = ''
    g_lsb = ''
    b_lsb = ''

    alpha = alpha.load()
    red = red.load()
    green = green.load()
    blue = blue.load()

    for y in range(height):
        for x in range(width):
            if alpha[x, y] != 255:
                r_lsb += str(red[x, y] & 0x1)
                g_lsb += str(green[x, y] & 0x1)
                b_lsb += str(blue[x, y] & 0x1)
    print(toString(r_lsb))
    print(toString(g_lsb))
    print(toString(b_lsb)) # ASCII: VolgaCTF{Tr@nspar3ncy_g1ves_fLag_aw@y!}

LSB_Check()
