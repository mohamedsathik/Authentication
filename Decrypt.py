from tkinter import *
from tkinter import messagebox as mb
import sys,os
from ByteHandler import *

def decryptBinFile(path,key):
    try:
        with open(path,"rb") as f:
            data = bytesDecrypt(f.read(),key)
        with open(path,"wb") as f:
            f.write(data)
        return True
    except Exception as e:
        print("error : ",e)
        return False

if(decryptBinFile(sys.argv[1],sys.argv[2])):
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    mb.showinfo("Success", "Your file has been decrypted Successfully.")
else:
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    answer = mb.askretrycancel(
        title='Authentication Failed',
        message='Unable to decrypt file.'
    )
    if answer:
        root.destroy()
        os.system("java FileCrypt")
    else:
        exit()

