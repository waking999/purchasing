
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.recordBtn = Button(self, text='Record', command=self.quit)
        self.recordBtn.pack()
        self.reportBtn = Button(self, text='Report', command=self.quit)
        self.reportBtn.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()

app.master.title('Purchasing Management System')

app.mainloop()