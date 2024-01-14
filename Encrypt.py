from tkinter import *
from tkinter import messagebox as mb
import sys,os
from ByteHandler import *

def encryptBinFile(path,key):
    try:
        with open(path,"rb") as f:
            data = bytesEncrypt(f.read(),key)
        with open(path,"wb") as f:
            f.write(data)
        return True
    except Exception as e:
        print("error : ",e)
        return False

print("hello")

if(encryptBinFile(sys.argv[1],sys.argv[2])):
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    mb.showinfo("Success", "Your file has been encrypted Successfully.")
else:
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    answer = mb.askretrycancel(
        title='Encryption Failed',
        message='Unable to encrypt file.'
    )
    if answer:
        root.destroy()
        os.system("java FileCrypt")
    else:
        exit()
