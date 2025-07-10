#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import messagebox
import urlcoder


def encode_text():
    text = input1.get("1.0", tk.END)
    if text[-1:] =='\n':
        text = text[:-1]
    text = urlcoder.url_encode(text.encode("utf-8"))
    display_text.delete(0.0, 'end')
    display_text.insert('end', text)


def decode_text():
    text = input1.get("1.0", tk.END)
    text = urlcoder.url_decode(text.encode("utf-8"))
    display_text.delete(0.0, 'end')
    display_text.insert('end', text)


def clear_text():
    input1.delete("1.0", tk.END)
    display_text.delete(0.0, 'end')


root = tk.Tk()
root.title("完美世界诸神之战 URL-Helper Version1.0")
root.geometry("380x450")

input1 = tk.Text(root, width=20, height=5)
input1.place(x=5, y=5, width=280, height=180)

button_en = tk.Button(root, text=u" 编 码 ", command=encode_text)
button_en.place(x=295, y=5, width=75, height=40)

button_de = tk.Button(root, text=u" 解 码 ", command=decode_text)
button_de.place(x=295, y=55, width=75, height=40)

button2 = tk.Button(root, text=" 清 空 ", command=clear_text)
button2.place(x=295, y=140, width=75, height=40)

label = tk.Label(root, text=" 转换结果")
#label.place(x=5, y=200, width=280, height=50)
label.pack(padx=5, pady=200, anchor='center')
display_text = tk.Text(root)
display_text.place(x=5, y=240, width=365, height=180)

root.mainloop()
