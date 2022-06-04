from tkinter import *
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry
import tkinter as tk

def lay_gia_tri(x):
    global a 
    a = a + str(x)
    text.set(a)
def xoa():
    global a 
    a = ""
    text.set(a)
def ketqua():
    global a 
    kq = str(eval(a))
    text.set(kq)
def back(): #ham tro lai 1 buoc
    global a 
    x = len(a)
    y = a[x-1]
    a=a.strip(y)
    text.set(a)
def dong_chuong_trinh():
    root.quit()
root = Tk()
root.title('may_tinh')
root.geometry('300x200')
a=""
text = StringVar()


entry = Entry(root,width = 50,textvariable = text).grid(columnspan=4)
cl = Button(root, text="xóa hết",command = xoa).grid(row=1, column=0)
bck = Button(root, text="lùi",command = back).grid(row=1, column=1)
lbl = Button(root).grid(row=1, column=2)   
close = Button(root, text="đóng",command = dong_chuong_trinh).grid(row=1, column=3) 
so7 = Button(root, text="7",command = lambda:lay_gia_tri(7)).grid(row=2, column=0) 
so8 = Button(root, text="8",command = lambda:lay_gia_tri(8)).grid(row=2, column=1) 
so9 = Button(root, text="9",command = lambda:lay_gia_tri(9)).grid(row=2, column=2)
chia = Button(root, text="/",command = lambda:lay_gia_tri('/')).grid(row=2, column=3) 
   
so4 = Button(root, text="4",command = lambda:lay_gia_tri(4)).grid(row=3, column=0) 
so5 = Button(root, text="5",command = lambda:lay_gia_tri(5)).grid(row=3, column=1) 
so6 = Button(root, text="6",command = lambda:lay_gia_tri(6)).grid(row=3, column=2) 
nhan = Button(root, text="*",command = lambda:lay_gia_tri('*')).grid(row=3, column=3) 
  
so1 = Button(root, text="1",command = lambda:lay_gia_tri(1)).grid(row=4, column=0) 
so2 = Button(root, text="2",command = lambda:lay_gia_tri(2)).grid(row=4, column=1) 
so3 = Button(root, text="3",command = lambda:lay_gia_tri(3)).grid(row=4, column=2) 
tru = Button(root, text="-",command = lambda:lay_gia_tri('-')).grid(row=4, column=3) 
  
so0 = Button(root, text="0",command = lambda:lay_gia_tri(0)).grid(row=5, column=0) 
cham = Button(root, text=".",command = lambda:lay_gia_tri(".")).grid(row=5, column=1) 
bang = Button(root, text="=",command = ketqua).grid(row=5, column=2) 
cong = Button(root, text="+",command = lambda:lay_gia_tri("+")).grid(row=5, column=3)

root.mainloop()