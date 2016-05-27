#!bash/bin/python

base16 = "0123456789abcdef"

def bin_to_hex(binary_string):
    
    temp = int(binary_string, 2)
    result = ""

    while temp != 0:
        result += base16[(temp % 16)]
        temp /= 16

    return result[::-1]


def hex_to_bin(hex_string):

    temp = int(hex_string, 16)
    result = ""

    while temp != 0:
        result += str(temp % 2)
        temp /= 2

    return result[::-1]

print bin_to_hex("111111")
print hex_to_bin("20")
