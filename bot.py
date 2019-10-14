import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
Los métodos con una '_' delante en el nombre son "privadas",
aunque esto no existe en python, pero nos sirve para aclararnos.
'''
class Compra:

    def __init__(self, prod, talla, color, type, mail, pag,
                 cc, cvv, venc, nombre,
                 dir, cp, ciudad, tel):

        def _url_pagina_seleccionada(nombre_pag):
            if(nombre_pag == 'Supreme'):
                return "https://www.supremenewyork.com/shop/all/" + self.type
            elif(nombre_pag == 'Amazon'):
                return "https://www.amazon.es"
            elif(nombre_pag == 'Adidas'):
                return "https://www.adidas.es"
            else: return -1

        def _venc_formateado(venc_crudo):
            mes, año = venc_crudo.split('/')
            return [mes,año]

        def _formato_dir(dir):
            calle, numero = dir.split(',')
            return [calle,numero]

        self.producto = prod
        self.talla = talla
        self.color = color
        self.type = type
        self.mail = mail
        self.url = _url_pagina_seleccionada(pag)
        self.cc = cc
        self.cvv = cvv
        self.venc = _venc_formateado(venc)
        self.nombre = nombre
        self.direccion = _formato_dir(dir)
        self.cp = cp
        self.ciudad = ciudad
        self.telefono = tel

def numero_enlaces(C):
    pagina = requests.get(C.url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    return(len(soup.find_all('a')))

def Busca_url_producto(C):
    pagina = requests.get(C.url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    for link in soup.find_all('a'):
        if link.string == C.producto and link.parent.next_sibling.contents[0].string == C.color:
            return link['href']

def dinerito(C):
    driver = webdriver.Chrome()
    driver.get("https://www.supremenewyork.com"+Busca_url_producto(C))
    elem = driver.find_element_by_name("commit")
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(elem)
    actions.click(elem)
    actions.perform()
    time.sleep(0.1)
    driver.get("https://www.supremenewyork.com/checkout")
    element = driver.find_element_by_id('order_billing_name')
    element.send_keys(C.nombre, Keys.TAB, C.mail,
    Keys.TAB, C.telefono, Keys.TAB, C.direccion[0], Keys.TAB,
    C.direccion[1], Keys.TAB, Keys.TAB, C.ciudad,
    Keys.TAB, C.cp, Keys.TAB, 'SP')
    element = driver.find_element_by_id('cnb')
    element.send_keys(C.cc, Keys.TAB, C.venc[0], Keys.TAB,
                      C.venc[1], Keys.TAB, C.cvv)
    element = driver.find_element_by_id('order_terms')
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(element)
    actions.click(element)
    actions.perform()
    driver.save_screenshot('screenshot.png')
    element = driver.find_element_by_name('commit')
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(element)
    actions.click(element)
    actions.perform()
    time.sleep(60)
    driver.close()
