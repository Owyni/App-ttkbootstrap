from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
import ttkbootstrap as ttk
import webbrowser
import tkinter as tk

root = ttk.Window(themename="superhero")
root.iconbitmap('Icono_app.ico')
root.iconbitmap(default='Icono_app.ico')
root.minsize(width=470, height=50)
root.maxsize(width=470, height=50)

root.title('Owynn')

toast = ToastNotification(title='Hey!',
                            message="angelaleman2212@gmail.com  :D",
                            alert=True,
                            duration=5000)

def callback(url):
    webbrowser.open_new(url)

def clicker():
    toast.show_toast()

def dark():
    root.style.theme_use('darkly')

def light():
    root.style.theme_use('flatly')

def exit():
    root.quit()

b1 = ttk.Button(root, text='LinkedIn', bootstyle=PRIMARY)
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/owyni/'))

b2 = ttk.Button(root, text='GitHub', bootstyle=SECONDARY)
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind('<Button-1>', lambda e: callback('https://github.com/Owyni'))

b3 = ttk.Button(root, text='Gmail', bootstyle=SUCCESS, command=clicker)   
b3.pack(side=LEFT, padx=5, pady=5)

b4 = ttk.Button(root, text='WebPage', bootstyle=INFO)
b4.pack(side=LEFT, padx=5, pady=5)

b7 = ttk.Button(root, text='light', bootstyle=LIGHT, command=light)
b7.pack(side=LEFT, padx=5, pady=5)

b8 = ttk.Button(root, text='dark', bootstyle=DARK, command=dark)
b8.pack(side=LEFT, padx=5, pady=5)

b6 = ttk.Button(root, text='Exit', bootstyle=DANGER, command=exit)
b6.pack(side=LEFT, padx=5, pady=5)

root.mainloop()
