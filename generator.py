def ascii_check(value):
    if (value < 32):
        return (value + 32)
    elif (value == 127):
       return (value - 1)
    else:
        return value

def cycle(keyword):
    head, *tail = keyword
    tail += head
    return tail

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def encode(letter, keyword):
    asc_num = (ord(letter) * ord(keyword[0]) ) % 128
    asc_num = ascii_check(asc_num)
    keyword = cycle(keyword)
    return (chr(asc_num), keyword)


def encrypt(plaintext, ciphertext, keyword):
    if (len(plaintext) == 0):
            return ciphertext
    else:
        letter, *l = plaintext

        c, keyword = encode(letter, keyword)
        ciphertext += c
        return encrypt(l, ciphertext, keyword)

def extend(password):
    if (len(password) < 16):
        password += password[::-1]
        return(password)


while True: 
    password = input("Enter Your Password: ")
    match password:
        case "":
            break
    keyword = input("Enter Website Name: ")
    match keyword:
        case "":
            break




    password = extend(password)

    print("Your encrypted password: ")
    print(encrypt(password, "", keyword))