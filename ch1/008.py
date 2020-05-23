import string


def cipher(s):
    lowercases = string.ascii_lowercase  # 全英小文字の文字列
    ciphered_s = ''
    for c in s:
        if c in lowercases:
            ciphered_s += chr(219 - ord(c))
        else:
            ciphered_s += c
            # print(ciphered_s)
    return ciphered_s


def decript_cipher(s):
    lowercases = string.ascii_lowercase
    decripted_s = ''


print('encription:', result := cipher('Hello, world!'))
print('decription:', cipher(result))
