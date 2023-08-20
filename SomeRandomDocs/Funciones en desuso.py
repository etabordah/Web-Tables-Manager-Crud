
from Modulo_base import Base
from Modulo_Bitacora import Registrar_dia
from Modulo_Perfiles import Perfiles_configurar
from Modulo_api import Api
from CONSTANTES import PSW
from CONSTANTES import BASES
from Modulo_inputs import wait
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
# from selenium import request

from selenium.webdriver.common.by import By

B=Base('admin',api=True)
print(B.eficiencia('2023-01-05', idejecutor=346))
# B.ir('instalacioneslocativa/instalacionlocativa/listar')


# B.find_element(By.ID,'display_ListaInstLocativaG_tipo').click()
# B.find_element(By.ID,'display_ListaInstLocativaG_tipo').click()

# masdel('instalacioneslocativa/instalacionlocativa/ver?idM=',[*range(150,300)])


def masspswd(url,ids):
    for i in ids:
        B.ir(url+str(i))
        try:
            B.find_element(By.ID,'cambiarPassword').click()
            B.find_element(By.ID,'btnAceptar').click()
            sleep(2)
        except:
            pass
    
             
# masspswd('cuentas/cuenta/editar?idM=',[*range(9,31)])
def masdel(url,ids):
    for i in ids:
        B.ir(url+str(i))
        try:
            B.find_element(By.ID,'accionb').click()
            B.find_element(By.ID,'btnAceptarModalPoP').click()
            sleep(2)
        except:
            pass


def sitemap(B,site={},link_prev=None):
    if link_prev!=None:
        B.ir(link_prev)

    links=[link.get_attribute('href') for link in B.find_elements(By.TAG_NAME,'a')]
    links=[link[len(B.weburl)+len('publico/'):] for link in links if link is not None and B.weburl in link]
    links=[link for link in links if not('ordenestrabajo/inicio/index' in link)]
    for i,link in enumerate(links):
        if '?' in link:
            links[i] = link[:link.index('?')]
        if '#' in link:
            links[i] = link.replace('#','')
    links = {link:link_prev for link in links if not(link in site)}
    for link in links:print(link)
    site.update(links)
    for link in links:
        try:
            site = sitemap(B,site,link)
        except:
            pass
    return site
# site=sitemap(B)
    
# B.is_open()
# # r=Registrar_dia('ET', '2022-04-01', B,until='2022-05-29')

# #######Copiar perfiles Amin
# # B1=Base(*BASES['CN1'])
# # B2=Base(*BASES['AMIN'])

# # Perfiles_configurar(B1, B2, 100)


# user=B.Record()


            
# def _sitemap_permisos(B,user):
#     from Modulo_inputs import inp
#     from Modulo_inputs import wait
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.common.keys import Keys
#     #Crear cuenta de usuario auxiliar - función pendiente
#     creds=[B.weburl,'a','a']
#     B_aux=Base(*creds)
    
#     t={k:v for k,v in B.mapa_perfiles.items() if 'Inventario/Almacenes' in k}
    
#     mp=B.mapa_perfiles
#     while user:
#         for k,p in t.items():
#             B.ir('/perfiles/perfil/editar?idM=104&pes=F1')
#             B.execute_script("Check('all', false);")
#             inp.ch(By.ID,B.mapa_perfiles[k]).Registrar(B, True)
#             B.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
#             wait.cl(B,By.ID,'btnAceptar')
            
#             while 'editar' in B.current_url:
#                 pass
            
#             for url in user:
#                 try:
#                     notif='NOTIFICACIÓN\nLa cuenta no tiene acceso a la página de inicio configurada. Comuníquese con el administrador del sistema.'
#                     while B_aux.find_element(By.ID,'mnt-message').text!=notif:
#                         B_aux.get(url)
#                         B_aux.login()
#                         pass
#                 except:
#                     pass
#                 # inp.txt(By.ID, 'contrasena').Registrar(B_aux, 'a',enter=True)
#                 inicio='https://demos.cloudmantum.com/consultoria1/publico/ordenestrabajo/inicio/index'
#                 if B_aux.current_url==url and not(inicio in B_aux.current_url):
#                     print(k,url)
#                     user.remove(url)
#                     B_aux.ir()
#                 B_aux.execute_script('javascript:redirigirSalir();')
                
# _sitemap_permisos(B,user)
