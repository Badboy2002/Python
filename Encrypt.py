# encoding = utf-8
"""
AES加密文件 支持文件(txt)
version1.3

"""
from Crypto.Cipher import AES


class MyAES(object):
    def __init__(self, mode=1):
        self.mode = mode

    def encrypt(self, rawtext, rawkey):
        #       去掉换行符,将字符串转换成字节
        text = rawtext.encode()
        key = rawkey.encode()
        #       用空字节填充至16位
        while len(text) % 16 != 0:
            text += b' '
        while len(key) % 16 != 0:
            key += b' '
        aes = AES.new(key, AES.MODE_ECB)
        encryptiontext = aes.encrypt(text)
        print("加密结果(二进制):", encryptiontext)          # 加密结果为二进制,不转成字符串
        return encryptiontext

    def decrypt(self, text, rawkey):
        key = rawkey.encode()
        while len(key) % 16 != 0:
            key += b' '
        aes = AES.new(key, AES.MODE_ECB)
        decryptiontext = aes.decrypt(text)
        print("解密结果(二进制):", decryptiontext)      # 解密结果为二进制
        decryptiontext_str = decryptiontext.decode()    # 转换成字符串
        decryptiontext_str = decryptiontext_str.strip()     # 去掉空格
        print("解密结果(字符串):", decryptiontext_str)
        return decryptiontext_str


filename = 'test.txt'
foo = MyAES()
f = open(filename, 'r', errors='ignore')
w = open('result.enc', 'wb')
line = f.read()
encode = foo.encrypt(line, "123456")
w.write(encode)
f.close()
w.close()


w = open('result.enc', 'rb')
putout = open('result.txt', 'w',)
print("------------分割线------------")
line = w.read()
de = foo.decrypt(line, "123456")
putout.write(de)
w.close()
putout.close()


