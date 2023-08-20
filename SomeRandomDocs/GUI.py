#ms-windows-store://pdp/?ProductId=9NRWMJP3717K
# implement pip as a subprocess:

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


def salir():
    root.destroy()
    root.quit()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    # python module to create GUI
    from tkinter import *
    import datetime
    
    root = Tk()
    root.title("MantumBot")
    root.geometry("1200x500")
    
    
    def encryptMessage():
        message = e1.get()
    
    
        # inbuilt function to encrypt a message
        ciphertext = onetimepad.encrypt(message, 'random')
        e2.insert(0, ciphertext)
    
    
    
    def decryptMessage():
        ciphertext = e3.get()
    
    
        # inbuilt function to decrypt a message
        decryptedMessage = onetimepad.decrypt(ciphertext, 'random')
        e4.insert(0, decryptedMessage)
    
    
    # lables = ['Modulo1', 'Modulo2']
    
    # for i, l in enumerate(lables):
    #     lbl = Label(root, text=l)
    #     lbl.grid(row=12+i, column=1)
    
    from Modulo_api import informe
    
    # # def test():
    # #     ev,ex = main()
    # #     h = reporte_desplazamientos(ev)
    # #     hh = reporte_horas(ev)
    
    # modules = {''}
    # creating labels and positioning them on the grid
    label1 = Label(root, text='Fecha inicio')
    label1.grid(row=10, column=1)
    label2 = Label(root, text= 'Fecha fin')
    label2.grid(row=11, column=1)
    # Label(root,text=os.getcwd()).grid(row=0,column=0)
    # l3 = Label(root, text="Ciphertext")
    # l3.grid(row=10, column=10)
    # l4 = Label(root, text="Decrypted message")
    # l4.grid(row=11, column=10)
    
    
    # creating entries and positioning them on the grid
    e1 = Entry(root)
    e1.grid(row=10, column=2)
    e1.insert(0,str(datetime.datetime.now())[:10])
    e2 = Entry(root)
    e2.grid(row=11, column=2)
    e2.insert(0,str(datetime.datetime.now())[:10])
    # e3 = Entry(root)
    # e3.grid(row=10, column=11)
    # e4 = Entry(root)
    # e4.grid(row=11, column=11)
    
    cal = 'ET'
    import sys
    
    def informe2():
        text_area.delete('1.0', END)
        sys.stdout = open('output.txt', 'w')
        fechainicio = e1.get()
        fechafin = e2.get()
        # print('Fechainicio: ',fechainicio)
        # print('Fechafin: ',fechafin)
        informe(cal, fechainicio, fechafin)
    
        with open('output.txt') as f:
            lines = f.readlines()
        # out 
        text_area.insert(INSERT,lines)
        
        
    from tkinter import scrolledtext
    text_area = scrolledtext.ScrolledText(root, wrap=WORD,
                                          width=90, height=15,
                                          font=("Times New Roman", 15))
      
    text_area.grid(column=20, row=20, pady=10, padx=10)
    
    # encryption button to produce the output
    encryptionButton = Button(root, text="Calcular Bitácora", bg="black", fg="white", command=informe2)
    encryptionButton.grid(row=13, column=2)
    
    
    # decryption button to produce the output
    decryptionButton = Button(root, text="Cerrar", bg="black", fg="white", command=salir)
    decryptionButton.grid(row=15, column=2)
    
    from Modulo_base import Base
    
    
    from Modulo_Bitacora import Registrar_dia
    decryptionButton = Button(root, text="Registrar", bg="black", fg="white", command=lambda: Registrar_dia(cal, e1.get(),
                                                                                                            Base('admin'),
                                                                                                            until=e2.get()))
    decryptionButton.grid(row=14, column=2)
    
    
    root.mainloop()
