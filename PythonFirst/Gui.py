#coding=utf-8
'''
Created on 2016年4月27日

@author: Administrator
'''
#from PIL import Image

from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text='Yeap!Say say say hello~~~')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit())
        self.quitButton.pack()
app = Application()
app.master.title('Rolling in the deep')
app.mainloop()