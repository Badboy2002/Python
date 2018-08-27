# encoding = utf-8
from Crypto.Cipher import AES
"""
AES加密文件 支持所有格式的文件
Version1.5 
"""

class FileAES (object):
    def __init__(self, filename):
        self.filename = filename

    def encrypt(self, key):
        readin = open(self.filename, 'rb')
        writeout = open(self.filename+'.enc', 'wb')
        ReadData = readin.read()
        while len(ReadData) % 16 != 0:   # 用空字节填充
            ReadData += b' '
        key = key.encode()
        while len(key) % 16 != 0:
            key += b' '
        ex = AES.new(key, AES.MODE_ECB)
        EncryptData = ex.encrypt(ReadData)
        writeout.write(EncryptData)
        readin.close()
        writeout.close()
        print(EncryptData)
        return EncryptData

    def decrypt(self, key):
        readin = open(self.filename+'.enc', 'rb')
        writeout = open('RE_'+self.filename, 'wb')
        ReadData = readin.read()
        key = key.encode()
        while len(key) % 16 != 0:
            key += b' '
        ex = AES.new(key, AES.MODE_ECB)
        DecryptData = ex.decrypt(ReadData)
        writeout.write(DecryptData)
        readin.close()
        writeout.close()
        print(DecryptData)
        return DecryptData

foo = FileAES('portablex86.rar')
foo.encrypt("123456")
foo.decrypt("123456")


