from tkinter import *


def new():
    print("hello")


def open_file():
    pass


def save():
    pass


def save_as():
    pass


# 窗口
root = Tk()  # 创建Tk对象
root.title("记事本")
root.geometry("500x300+600+300")  # 更改窗口大小+位置
# 菜单
me = Menu()  # 创建菜单
root.config(menu=me)
file_menu = Menu(me)  # 二级菜单
file_menu.add_command(label="新建", accelerator='Ctrl+N', command=new)
file_menu.add_command(label="打开", accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label="保存", accelerator='Ctrl+S', command=save)
file_menu.add_command(label="另存为", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="页面设置")
file_menu.add_command(label="打印")
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)
me.add_cascade(label="文件", menu=file_menu)
# 编辑区
text = Text()  # 多行文本框
text.pack(expand=YES, fill=BOTH)

root.mainloop()  # 窗口结束
