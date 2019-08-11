import tkinter as tk
from tkinter import ttk
from tkinter import *
import model.DBOperation as dbo


class ItemManagement:
    def __init__(self):
        self.db = dbo.DBOpeation()
        self.rowHeight=20
        self.changeStatus=None


    def show(self,rootWin):
        self.rootWin = rootWin
        self.itemMgtWin = tk.Toplevel(rootWin)
        self.itemMgtWin.geometry('400x300')
        self.itemMgtWin.title('Item Management')


        self.rows = self.db.getAllItems()
        height = len(self.rows)
        self.columns = ("ID", "Name", "IS_VALID")
        self.colWidths = [20, 300, 60]
        self.colStarts = [0, 20, 320]

        self.tree = ttk.Treeview(self.itemMgtWin, height=height, show="headings", columns=self.columns)

        self.tree.column("ID", width=self.colWidths[0], anchor='w')
        self.tree.column("Name", width=self.colWidths[1], anchor='w')
        self.tree.column("IS_VALID", width=self.colWidths[2], anchor='w')

        #self.tree.heading("ID", text="ID")  # 显示表头
        #self.tree.heading("Item Name", text="Item Name")
        #self.tree.heading("VALID", text="valid")

        for col in self.columns:  # bind function to make the header sortable
            self.tree.heading(col, text=col, command=lambda _col=col: self.sortColumn(self.tree, _col, False))

        for i in range(height):  # Rows
            self.tree.insert("", i, values=self.rows[i])


        self.tree.bind('<Double-1>', self.setCellValue)  # Double-click the left button to enter the edit
        self.newItemBtn = ttk.Button(self.itemMgtWin, text='New Item', width=20, command=self.newRow)
        self.newItemBtn.place(x=120, y=(height) * self.rowHeight + 45)
        self.tree.pack(side=LEFT, fill=BOTH)

    def sortColumn(self, tv,  col, reverse):  # Treeview, column name, arrangement
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # Sort by
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # based on sorted index movement
            tv.move(k, '', index)
            tv.heading(col, command=lambda: self.sortColumn(tv, col, not reverse))  # Rewrite th

    def setCellValue(self, event):  # Double click to enter the edit state
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            column = self.tree.identify_column(event.x)  # column
            row = self.tree.identify_row(event.y)  # row

        self.editCN = int(str(column).replace('#', ''))
        if self.editCN==1:
            return

        self.editRN = int(str(row).replace('I', ''))
        print(self.editCN)
        entryedit = Text(self.itemMgtWin, width=self.colWidths[self.editCN-1], height=1)
        entryedit.place(x=self.colStarts[self.editCN - 1], y=6 + self.editRN * 20)

        def saveedit():
            self.tree.set(item, column=column, value=entryedit.get(0.0, "end"))
            self.rows[self.editRN-1][self.editCN-1]=entryedit.get(0.0, "end")[:-1]
            entryedit.destroy()
            okb.destroy()
            print(self.rows)
            if self.changeStatus!='new':
                self.db.update("item",[self.columns[self.editCN-1]],[self.rows[self.editRN-1][self.editCN-1]],self.rows[self.editRN-1][0])
            else:
                self.db.insert("item",self.columns,self.rows[self.editRN-1])

            self.changeStatus=None

        okb = ttk.Button(self.itemMgtWin, text='OK', width=4, command=saveedit)
        okb.place(x=self.colStarts[self.editCN], y=2 + self.editRN * 20)


    def newRow(self):
        height = len(self.rows)
        self.rows[height]=[height+1,'',1]
        self.tree.insert('', height, values=(height +1, '',1))
        self.tree.update()
        self.newItemBtn.place(x=120, y=(height + 1) * 20 + 45)
        self.newItemBtn.update()
        self.changeStatus='new'

