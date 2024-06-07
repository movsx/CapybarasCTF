# Решение Reverse 2 От Макса, до конца не работает
from pprint import pprint

def scissors(input_str):
    res = []
    for i in range(0, len(input_str), 2):
        res.append(input_str[i: i + 2])
    return res

def rotate_str(input_str, key):
    string_list = scissors(input_str)
    values = []
    for i in range(0, len(string_list)):
        index = (i + key) % len(string_list)
        values.append(string_list[index])
    return ''.join(i for i in values)

def xorstr(input_str, key):
    string_list_1 = scissors(input_str)
    string_list_2 = scissors(key)
    res = ''
    for i in range(0, len(string_list_1)):
        int1 = int(string_list_1[i], 16)
        int2 = int(string_list_2[i], 16)
        xorchik = hex(int1 ^ int2)[2:]
        if len(xorchik) == 1:
            xorchik = '0' + xorchik
        if len(xorchik) == 0:
            xorchik = '00'
        res += xorchik
    return res

real_mases = []

mas = "77bb234face137c4ad1e61efc0f4f6eeee6f4f0cfe16e1da4c731ecaf432bb77"
real_mases.append(mas)
for i in range(0, len(mas), 2):
    rotate_key = int(mas[i:i + 2], 16)
    mas = rotate_str(mas, rotate_key)
    real_mases.append(mas)

real_mases = real_mases[::-1]

pprint(real_mases)
input_data = "B7B04EB788419838EEDEF75AAF9B4534A764AD7EF4AD4D943B3090F4968A72".lower()
for i in real_mases:
    input_data = xorstr(input_data, i)
    print(input_data)
