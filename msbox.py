# Python program to create
# yes/no message box


import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


def call():
	res = mb.askquestion('Exit Application',
						'Do you really want to exit')
	
	if res == 'yes' :
        print("hi")
		#root.destroy()
        # print("hi")
		
	else :
		mb.showinfo('Return', 'Returning to main application')

# Driver's code

