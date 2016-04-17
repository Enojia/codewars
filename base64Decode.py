#!/bash/python

def base64_to_base10(string):
    base64Dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    num = 0
    for i in range(0, len(string)):
        num *= 64
        num += (base64Dict.index(string[i]))

    print num


number = "CA"

base64_to_base10(number)
