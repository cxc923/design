# -*- coding:utf-8 -*-
# Author : CXC
# Data : 2019/8/14 12:17


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from PIL import ImageTk


def Fonts(*args):
    # 构造字体选择
    font = {'仿宋': '331', '艺术体': '364', '明星手写体': '5', '马卡龙': '383', '雁翔': '4', '太极文': '306', '舒同': '13',
            '行楷繁': '9', '清韵字体': '310'}
    return font[comboxlist1.get()]


def Get_sign():
    startUrl = 'http://www.yishuzi.com/b/re13.php'
    name = Entry1.get()
    name = name.strip()
    if name == "":
        messagebox.showinfo('提示', '请输入需要设计的名称')
    else:

        fontsIndex = Fonts()  # 索引

        # 模拟浏览器post数据，浏览器里面的关键索引
        data = {
            'id': name,
            'idi': 'jiqie',
            # 文字索引
            'id1': fontsIndex,
            # 'id2': bgcolor,
            'id2': '#FFFDFA',
            'id3:': '',
            # 签字的配色
            'id4': '#EBFFFC',
            'id5': '',
            # 'id6': 字体颜色
            'id6': '#2AA863'
        }

        result = requests.post(startUrl, data=data)
        result.encoding = 'utf-8'
        html = result.text
        print(html)

        # 通过正则表达式获取设计好的图片
        pat = '<img src="(.*?)">'
        pat = re.compile(pat)
        imgPath = re.findall(pat, html)

        response = requests.get(imgPath[0]).content
        with open('{}.gif'.format(name), 'wb') as f:
            f.write(response)

        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
        # 放置返回的图片
        label2 = Label(window, image=bm)
        label2.bm = bm
        label2.place(height=272, width=440, x=60, y=140)


def clean():
    name = Entry1.get()
    name = name.strip()
    if name == "":
        messagebox.showinfo('提示', '别点了，没有数据！！！')
    Entry1.delete(0, END)


def window_quit():
    messagebox.showinfo('小提示', '设计好的图片和程序在同一路径下，自行筛选。')
    window.quit()


if __name__ == '__main__':
    # 1.创建一个窗口
    window = tk.Tk()
    # 2.指定窗体名称
    window.title("签名设计v1.0")
    # 3.指定窗体大小
    window.geometry('800x500')
    # 4.禁止最大窗口
    # windows.resizable(0, 0)

    Label1 = tk.Label(window, text='名称:  ', font=('华文新魏', 15), fg='black')
    Label1.grid(row=0)
    Entry1 = tk.Entry(window, font=('华文行楷', 25))
    Entry1.grid(row=0, column=1)

    # 字体模式
    Label2 = tk.Label(window, text='字体选择 ', font=('华文中宋', 10), fg='red')
    Label2.place(height=44, width=127, x=470, y=100)
    var1 = tk.StringVar()
    comboxlist1 = ttk.Combobox(window, textvariable=var1)
    comboxlist1['values'] = ("仿宋", "艺术体", "明星手写体", "马卡龙", "雁翔", "太极文", "舒同", "行楷繁", "清韵字体")
    comboxlist1.current(0)  # 选择第一个
    comboxlist1.bind("<<ComboboxSelect>>", Fonts)  # 绑定数据
    comboxlist1.place(height=30, width=100, x=570, y=107)
    # Listbox1=tk.Listbox(windows)
    # Listbox1.place(height = 30,width = 100,x = 480,y = 107)
    Button1 = tk.Button(window, text='签名设计', font=('隶书', 15), command=Get_sign)
    Button1.place(height=30, width=100, x=60, y=82)
    Button2 = tk.Button(window, text='退出软件', font=('隶书', 15), command=window_quit, fg='red')
    Button2.place(height=30, width=100, x=204, y=82)
    Button3 = tk.Button(window, text='清空', font=('隶书', 15), command=clean, fg='black')
    Button3.place(height=30, width=70, x=500, y=10)
    window.mainloop()
