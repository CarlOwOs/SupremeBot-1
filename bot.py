from bs4 import BeautifulSoup
import requests

'''
Los métodos con una '_' delante en el nombre son "privadas",
aunque esto no existe en python, pero nos sirve para aclararnos.
'''
class Compra:

    def __init__(self, prod, talla, mail, pag,
                 cc, cvv, venc, nombre,
                 dir, cp, ciudad):

        def _url_pagina_seleccionada(nombre_pag):
            if(nombre_pag == 'Supreme'):
                return "https://www.supremenewyork.com/shop"
            elif(nombre_pag == 'Amazon'):
                return "https://www.amazon.es"
            elif(nombre_pag == 'Adidas'):
                return "https://www.adidas.es"
            else: return -1

        def _venc_formateado(venc_crudo):
            mes, año = venc_crudo.split('/')
            return [mes,año]

        #devuelve un vector con el nombre en la primera posición y los apellidos
        #en las siguientes.
        def _formato_nombre(nombre_completo):
            return nombre_completo.split()

        self.producto = prod
        self.talla = talla
        self.mail = mail
        self.url = _url_pagina_seleccionada(pag)
        self.cc = cc
        self.cvv = cvv
        self.venc = _venc_formateado(venc)
        self.nombre = _formato_nombre(nombre)
        self.direccion = dir
        self.cp = cp
        self.ciudad = ciudad

def numero_enlaces(C):
    pagina = requests.get(C.url)
    soup = BeautifulSoup(pagina.content)
    soup.find_all('a')
