import tkinter as tk
import os

"""
This is a GUI implementation of the button.py script, used to start and stop the 
pimoroni-fanshim.service using FanSHIM's button.
"""

#defining the main window and configuring it
root = tk.Tk()
root.title('Pimoroni FanSHIM')
root.geometry('240x70')
root.resizable(False, False)

#defining the start and stop commands

def press():
	os.system('sudo systemctl stop pimoroni-fanshim.service')

def hold():
	os.system('sudo systemctl start pimoroni-fanshim.service')


#defining the buttons
off = tk.Button(text = 'stop pimoroni-fanshim.service', command = press)
on = tk.Button(text = 'start pimoroni-fanshim.service', command = hold)

#placing the buttons on screen
off.pack()
on.pack()

#ending the mainloop
root.mainloop()
