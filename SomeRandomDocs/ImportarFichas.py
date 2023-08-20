import os
import pandas as pd
import openpyxl
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from Modulo_base import Base
import time
from math import isnan
import datetime

def __checkvals(v):
    k_out = {}
    for k, val in v.items():
        if val == "":
            continue
        if isinstance(val,datetime.datetime):
            val = val.isoformat().split("T",1)[0]
        if isinstance(val, float):
            if isnan(val):
                continue
        if val == 'Na':
            continue
        k_out.update({k:val})
    return k_out

def __registrar(B,url,i,v,f,times = 5):
    try:
        B.ir(url+str(i))
        B.execute_script('PopUP.MostrarForm("%s");' % f)
        v = __checkvals(v)
        print(v)
        B.Registrar_mult(dict(v))
        if not("ver" in url):
            B.aceptar()
        time.sleep(1)
    except:
        if times > 0:
            times-= 1
            __registrar(B, url, i, v, f,times=times)
        print('Error',i,v)
        
def registrarFicha(B, ficha, cerrar=False, demos=False):
    if isinstance(B,str):
        B = Base(B,demos=demos)
        cerrar = True
    for f in openpyxl.load_workbook(ficha).sheetnames:
        url = pd.read_excel(ficha,f).columns[0]
        L = pd.read_excel(ficha,f,skiprows=1,index_col=0)
        for i, v in L.iterrows():
            __registrar(B, url, i, v, f)
            # try:
            #     B.ir(url+str(i))
            #     B.execute_script('PopUP.MostrarForm("%s");' % f)
            #     B.Registrar_mult(dict(v))
            #     if not("ver" in url):
            #         B.aceptar()
            #     time.sleep(1)
            # except:
            #     print('Error',v)
        time.sleep(1)
    if cerrar:
        B.quit()

if __name__ == "__main__":
    B = 'sistemasinteligentesenred'
    ficha = "SIER-FichaPersonalComplementaria.xlsx"
    demos = 0
    f='F2'
    L = pd.read_excel(ficha,f,skiprows=1,index_col=0)
    v = L.iloc[20]
    v = __checkvals(v)
    print(v)
    # registrarFicha(base, xls,demos=0)