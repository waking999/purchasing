
import tkinter as tk
import view.ItemManagement as imw



class Application:
    def __init__(self):
        self.window=tk.Tk();


    def showWindow(self):
        # 第2步，给窗口的可视化起名字
        self.window.title('Purchasing Management System')

        # 第3步，设定窗口的大小(长 * 宽)
        self.window.geometry('400x300')  # 这里的乘是小x

        self.reportBtn = tk.Button(self.window, text='Item Management', command=self.itemMgt)
        self.reportBtn.place(x=120, y=240)

        # 第10步，主窗口循环显示
        self.window.mainloop()

    def itemMgt(self):
        itemMgtWin=imw.ItemManagement()
        itemMgtWin.show(self.window)

app=Application()
app.showWindow()






