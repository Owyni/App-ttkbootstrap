from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

root = ttk.Window(themename="superhero")
root.title('Owynn probando cosas')

root.title('Owynn')
root.iconbitmap('Icono_app.ico')
root.iconbitmap(default='Icono_app.ico')
root.geometry('300x200')

def clicker():
    toast.show_toast()

toast = ToastNotification(title='Hi!',
                          message="Hola, soy Owynn ",
                          duration=3000,
                          alert=True,
                          position= 'south west',
                          )

my_botton = ttk.Button(root, text='Click me', command=clicker)
my_botton.pack(pady=40)

root.mainloop()