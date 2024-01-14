from bitcoin import *
import binascii

from matplotlib.pyplot import fill

def getBytes(inp):
    return [[j for j in binascii.unhexlify(encode_privkey(i,'hex'))] for i in privtopub(encode_privkey(sha256(inp),"decimal"))]
    
def bytesAdd(x, y):
    l = (len(y[0]) + len(y[1]))//2
    c = 0
    s = 1
    for i in range(len(x)):
        if c == l:
            c = 0
            s += 1
        a = (y[0][c] * s) % 256
        b = (y[1][c] * s) % 256
        x[i] =  (x[i] + a + b) % 256
        c += 1
    return x

def bytesSub(x,y):
    l = (len(y[0]) + len(y[1]))//2
    c = 0
    s = 1
    for i in range(len(x)):
        if c == l:
            c = 0
            s += 1
        a = (y[0][c] * s) % 256
        b = (y[1][c] * s) % 256
        x[i] =  (x[i] - a - b) % 256
        c += 1
    return x


from Encrypt import key_encrypt,encode,decode,encrypt,decrypt,key_decrypt

def fillEmpty(d):
    l = len(d)
    for i in range(512-l):
        d.append(0)
    for n in range(-3,0):
        if(l > 0):
            if l > 255:
                l  = l - 255
                d[n] = 255
            else:
                d[n] = l
                l = l - 255
    return d

def bytesEncrypt(bdata,passw):
    e = fillEmpty([i for i in binascii.unhexlify(encrypt(key_encrypt("012345678",sha256(passw),256),16))])
    p = sha256(passw)
    x = [i for i in bdata]
    y = getBytes(p)
    z = bytesAdd(x,y)
    return bytes(z + e)

def bytesDecrypt(bdata,passw):
    l = len(bdata)
    key_decrypt(decrypt(bytes(bdata[l-512:-1][:bdata[-1] + bdata[-2] + bdata[-3]]).hex(),16),sha256(passw),256)
    p = sha256(passw)
    x = [i for i in bdata[:l-512]]
    y = getBytes(p)
    z = bytesSub(x,y)
    return bytes(z)

e = encrypt(key_encrypt("012345678",sha256("1"),256),16)
b = binascii.unhexlify(e)
b = [i for i in b]

with open("/home/praveen/Downloads/251380-ubuntu-wallpaper-3d-lantern.jpg","rb") as f:
    e = bytesEncrypt(f.read(),"hello")

print(len(e))

bytesDecrypt(e,"hello")