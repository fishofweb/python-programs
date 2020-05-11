print("Welcome to CIPHER App.\n")

cipher_codes = {
    'a': '12s',
    'b':'aqw',
    'c':'cd',
    'e':'6yu',
    'f':'tgf',
    'g':'zxs',
    'h':'poi',
    'i':'tee',
    'j':'mkc',
    'k':'rrv',
    'l':'jjn',
    'm':'ooo',
    'n':'vvt',
    'o':'cxx',
    'p':'12u',
    'q':'nb0',
    'r':'drz',
    's':'ssa',
    't':'jjj',
    'u':'iii',
    'v':'wqb',
    'w':'c23',
    'x':'pss',
    'y':'2g2',
    'z':'3uu',
        }

choice = input("Do you want to encode/decode your message:\n ")
start = 0
stop = 3
if choice == 'encode':
    message = input("Type to ecode your message: ")
    message = list(message)
    print(message)
    for k,v in cipher_codes.items():
        for i in message:
            if i == k:
                print(v, end="")

elif choice == 'decode':
    decode_list = []
    message = input("Type to decode your message: ")
    message = list(message)
    str1 = ""
    # print(message)
    for c in message:
        a = message[start:stop]
        for b in a:
            str1 += b
        print(str1)
        decode_list.append(str1)
        print
        start += 3
        stop +=3

    # for k,v in cipher_codes.items():




    # for k, v in cipher_codes.items():
    #     for j in range(len(decode_list)):
    #         if decode_list[j] == v:
    #             print(k, end="")