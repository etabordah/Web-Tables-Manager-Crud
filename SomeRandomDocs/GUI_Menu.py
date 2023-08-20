try:
    import sys
    import subprocess
    import pandas
    import webdriver_manager
    import tk
    import google
    import openpyxl
    import tqdm
except:
        
    pkgs = ['pandas','google','google-api-python-client','openpyxl',
            # '-upgrade google-api-python-client',
            'google_auth_oauthlib','selenium','tk','webdriver_manager','tqdm']
    for p in pkgs:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', p])
    
import os

import tkinter as tk
from tkinter import filedialog
from ImportarFichas import registrarFicha
from GUI import salir
import types
from tkinter import Tk
import datetime
from tkinter import *



class window(Tk):
    def salir(self):
        self.destroy()
        self.quit()
        
    def __init__(self,labels,pos):
        super().__init__()
        self.title("MantumBot - Cargar Fichas")
        self.geometry("200x"+str(len(labels)*28))
        i = 1
        params = {}
        for lbl,tipo in labels.items():
            if not(isinstance(tipo,types.FunctionType) or isinstance(tipo,list)):
                tk.Label(self, text = lbl).grid(row=i, column=pos[tipo]) 
            if isinstance(tipo,list):
                clicked = StringVar()
                clicked.set(tipo[0])
                drop = OptionMenu( self , clicked , *tipo )
                drop.grid(row=i,column=2)
                params.update({lbl:clicked})
            if tipo == 'campo':
                e = tk.Entry(self)
                e.grid(row=i, column=pos[tipo]+1)
                params.update({lbl:e})
            if tipo == 'check':
                var = tk.IntVar()
                chk = tk.Checkbutton(self, text="demos", variable=var)
                chk.grid(row=i,column=pos[tipo])
                params.update({lbl:var})
            if isinstance(tipo,types.FunctionType):
                button = tk.Button(self, text=lbl, command=tipo)
                button.grid(row= i, column= 2)
            i += 1
        tk.Button(self, text='Cerrar', command=lambda: self.salir()).grid(row=i,column=1)
        self.params = params
    


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename,params['demos'].get(),params['base'].get())
    registrarFicha(params['base'].get(), filename,demos=params['demos'].get())

labels = {
    '~ Acciones Masivas ~':'titulo',
    '~ Mántum ~':'titulo',
    'base':'campo',
    'demos':'check',
    'Cargar Ficha':UploadAction,
    '~ Registrar bitácora ~':'titulo',
    'Calendario':[
            "ET",
            "JU",
            "JR",
            "RR",
            "DO",
        ],
    'Fecha Inicio':'campo',
    'Fecha Fin':'campo',
    'Calcular':UploadAction,
    'Registrar':UploadAction
    }

pos = {
       'titulo':2,
       'campo':1,
       'check':2
       }
root = window(labels, pos)
params={}

setattr(root, 'UploadAction', UploadAction)


root.params['Fecha Inicio'].insert(0,str(datetime.datetime.now())[:10])
root.params['Fecha Fin'].insert(0,str(datetime.datetime.now())[:10])

root.mainloop()





