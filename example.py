from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
'''
driver = webdriver.Chrome()
driver.get("https://www.google.es")

element = driver.find_element_by_name('q')
element.clear()
element.send_keys('Como ganar la HACK UPC', Keys.ENTER)

driver.close()

'''
class Compra:

    def __init__(self, prod, talla, mail, pag,
                 cc, cvv, venc, nombre,
                 dir, cp, ciudad):

        def _url_pagina_seleccionada(nombre_pag):
            if(nombre_pag == 'Supreme'):
                return "https://www.supremenewyork.com/shop/all/tops_sweaters"
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

def Busca_url_producto(C):
    pagina = requests.get(C.url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    for link in soup.find_all('a'):
        if link.string == C.producto:
            if link.parent.next_sibling.contents[0].string == "Black":
                return link['href']


C = Compra("Textured Stripe Polo", "S", "Black", "tops_sweaters" "megaelius4@gmail.com", "Supreme",
               "0000 1111 2222 3333", "123", "01/2020", "Pepito Pérez",
               "Calle arriba 1", "03300", "Orihuela")

driver = webdriver.Chrome()
driver.get("https://www.supremenewyork.com"+Busca_url_producto(C))
elem = driver.find_element_by_name("commit")
actions = webdriver.ActionChains(driver)
actions.move_to_element(elem)
actions.click(elem)
actions.perform()
#driver.implicitly_wait(3)
time.sleep(1)
driver.get("https://www.supremenewyork.com/checkout")
element = driver.find_element_by_id('order_billing_name')
element.send_keys('Pepito', Keys.TAB, 'pepito@gmail.com',
Keys.TAB, '696914140', Keys.TAB, 'c/UPC Campus Nord', Keys.TAB,
'A5102', Keys.TAB, 'Barcelona, ESPAÑA', Keys.TAB, 'Barcelona',
Keys.TAB, '03300', Keys.TAB, 'SP')
element = driver.find_element_by_id('cnb')
element.send_keys(C.cc, Keys.TAB, C.venc[0], Keys.TAB,
                  C.venc[1], Keys.TAB, C.cvv)
element = driver.find_element_by_id('order_terms')
actions = webdriver.ActionChains(driver)
actions.move_to_element(element)
actions.click(element)
actions.perform()
