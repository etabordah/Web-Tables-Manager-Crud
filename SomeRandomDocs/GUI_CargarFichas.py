import tkinter as tk
from tkinter import filedialog
from ImportarFichas import registrarFicha
from GUI import salir

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename,var.get(),e1.get())
    registrarFicha(e1.get(), filename,demos=var.get())

root = tk.Tk()
root.title("MantumBot - Cargar Fichas")
root.geometry("200x150")
label1 = tk.Label(root, text='~ Acciones Masivas ~')
label1.grid(row=1, column=2)
label1 = tk.Label(root, text='~ Mántum ~')
label1.grid(row=2, column=2)
label1 = tk.Label(root, text='base')
label1.grid(row=3, column=1)
var = tk.IntVar()
chk = tk.Checkbutton(root, text="demos", variable=var)
chk.grid(row=4,column=2)
e1 = tk.Entry(root)
e1.grid(row=3, column=2)
button = tk.Button(root, text='Cargar Ficha', command=UploadAction)
button.grid(row= 5, column= 2)
tk.Button(root, text='Cerrar', command=lambda: salir(root)).grid(row=6,column=1)

root.mainloop()