# -*- coding:utf-8 -*-

# 导入tkinter包
from tkinter import *

# 从Frame派生一个Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLable = Label(self, text = 'hello,world!' )
        self.helloLable.pack()
        self.quitButton = Button(self, text = 'Quit', command=self.quit)
        self.quitButton.pack()

# 实例化Application，并启动运算
app = Application()
# 设置窗口标题
app.master.title('hello world')
# 主消息循环
app.mainloop()