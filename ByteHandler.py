import binascii,ast
from bitcoin import encode_privkey,privtopub,sha256,ripemd160,hex_to_b58check


code_strings = {2: '01',8: '012345678',10: '0123456789',16: '0123456789abcdef',32: 'abcdefghijklmnopqrstuvwxyz234567',58: '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
64: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/',85: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~',
91: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+,./:;<=>?@[]^_`{|}~-',256: ''.join([chr(x) for x in range(256)])
}
s = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
d = "0123456789"
pt = "!#$%&()*+,./:;<=>?@[]^_{|}~-"
digits = ["0","1","2","3","4","5","6","7","8","9"]
p = ["~","!","@","#","$","%","^","&","*","(",")","_","-","+","+","{","}","[","]","|",":",";","<",">",".",",","?"
    "/"]
l11l = 0
ll1l = 1
ll = ll1l + ll1l
l1 = ll * ll
lll = l1 * ll
l1l = lll * ll 
l11 = lll * l1l
l111 = ll1l + ll1l
lll1 = l111 * l11l 
llll = l111 + lll1
l1ll = l111 + ll1l
l1111 =  ll * l1 * lll * l1l * l11 * l111 * l1ll * llll
l1l1l =  llll + l1ll + l111 + l11 + l1l + lll + l1 + ll
ll11l = l1111 * l1l1l
l111l = ll11l * l1l1l * l1111 * l1l1l
lllll = ll11l * l1l1l * l1111 * l1l1l * l111l
def digest(ll,l1):
  ll1 = ll * llll
  lll = str(l1)[:: -1]
  lll = int(lll)
  l = len(str(lll))
  if lll % l111 == lll1 :
    l1l = llll
  else :
    l1l = l1ll
  if l % l111 == lll1:
    l1 = l1l * l1ll * l
  else:
    l1 = l1l * llll * l
  l11l = ll1 * lll * lllll
  ll1l = lll // l1
  return l11l * ll1l * lll
def vomit(ll,l1):
  ll1 = ll // llll
  lll = str(l1)[:: -1]
  lll = int(lll)
  l = len(str(lll))
  if lll % l111 == lll1 :
    l1l = llll
  else :
    l1l = l1ll
  if l % l111 == lll1:
    l1 = l1l * l1ll * l
  else:
    l1 = l1l * llll * l
  l11l = ll1 // lll // lllll
  ll1l = lll // l1
  return l11l // ll1l // lll
def xdigest(ll,l1):
  ll = ll
  l1 = int(str(l1)[:: -1])
  return ll * l1
def xvomit(ll,l1):
  ll = ll
  l1 = int(str(l1)[:: -1])
  return ll // l1

def BinaryToDecimal(binary):
    binary = str(binary) 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return decimal

def get_code_string(b):
    return code_strings[b]

def DecimalToBinary(decimal):       
    if decimal > 1: 
        DecimalToBinary(decimal // 2) 
    binary = bin(int(decimal)).replace("0b", "")
    return binary

def encode(val, base = 16 , minlen=1):
    base, minlen = int(base), int(minlen)
    code_string = get_code_string(base)
    result = ""
    while val > 0:
        result = code_string[val % base] + result
        val //= base
    return code_string[0] * max(minlen - len(result), 0) + result

def decode(string, base = 16 ):
    base = int(base)
    code_string = get_code_string(base)
    result = 0
    if base == 16:
        string = string.lower()
    while len(string) > 0:
        result *= base
        result += code_string.find(string[0])
        string = string[1:]
    return result

def serialize(json):
    x = decode(str(json),256)
    return encode(x,64)

def deserialize(string):
    x = decode(string,64)
    return ast.literal_eval(encode(x,256))

def encryption(text):
    text = str(text)
    x = text.encode('utf-8')
    bin = binascii.hexlify(x)
    y = bin.decode('utf-8')
    z = decode(y)
    return z

def decryption(val):
    x = encode(int(val))
    bin = x.encode('utf-8')
    y = binascii.unhexlify(bin)
    z = y.decode('utf-8') 
    return z

def encrypt(text,base=91):
    x = encryption(text)
    d = encode(x,base)
    if base == 10 or base == 2 :
        return int(d)
    else:
        return d

def decrypt(value,base=91):
    x = decode(str(value),base)
    return decryption(x)

def key_encrypt(text,key,base):
    x = encrypt(text,10)
    y = encrypt(hex_to_b58check(ripemd160(str(key)))[1:],10)
    return encrypt(digest(x,y),base)

def key_decrypt(text,key,base):
    x = int(decrypt(text,base))
    y = encrypt(hex_to_b58check(ripemd160(str(key)))[1:],10)
    return decrypt(vomit(x,y),10)

def get_privkey(_phrase):
    if type(_phrase) == list :
        x = ' '.join(i for i in _phrase)
        return ripemd160(sha256(x))
    elif type(_phrase) == str:
        return ripemd160(sha256(_phrase))

def is_key(key):
      if len(key) == 40 :
            validator = list(code_strings[16])
            for i in key:
                  if i not in validator:
                        return False
            return True       
      return False

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