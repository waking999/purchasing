import tkinter as tk
from tkinter import *

import model.DBOperation as dbo

class AddOrder:
    def __init__(self):
        self.db = dbo.DBOpeation()



    def show(self,rootWin):
        self.rootWin = rootWin
        self.addOrderWin = tk.Toplevel(rootWin)
        self.addOrderWin.geometry('400x300')
        self.addOrderWin.title('Add Order')





        self.dateLabelWidget =Label(self.addOrderWin,text = 'Date')
        self.dateLabelWidget.pack()
        self.dateWidget =  Text(self.addOrderWin, width=20, height=1)
        self.dateWidget.pack()
        self.realRateLabelWidget = Label(self.addOrderWin, text = 'Real Rate')
        self.realRateLabelWidget.pack()
        self.realRateWidget =Text(self.addOrderWin, width=20, height=1)
        self.realRateWidget.pack()

        # Create a Tkinter variable
        tkvar = StringVar(self.addOrderWin)

        # Dictionary with options
        choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
        tkvar.set('Pizza')  # set the default option


        self.itemLabelWidget=Label(self.addOrderWin, text="Choose a dish")
        self.itemLabelWidget.pack()
        popupMenu = OptionMenu(self.addOrderWin, tkvar, *choices)
        popupMenu.pack()
