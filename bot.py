from tkinter import *
from tkinter.ttk import *

class Compra:
    def _vec
    def __init__(self, prod, talla, mail, pag, cc, cvv, venc, nombre, dir, cp, ciudad):
        self.producto = prod
        self.talla = Talla
        self.mail = mail
        self.url =
        self.cc = cc
        self.cvv = cvv
        self.venc = venc
        self.nombre = nombre
        self.direccion = dir
        self.cp = cp
        self.ciudad = ciudad

    def agregar_truco(self, truco):
        self.trucos.append(truco)

def comprar():
    print("vamosssss")

def main():

    window = Tk()
    window.title("SupremeBot")
    window.geometry('400x400')
    lbl_prod = Label(window, text="Nombre del producto:")
    lbl_prod.grid(column=0, row=0)
    txt_prod = Entry(window,width=40)
    txt_prod.grid(column=1, row=0)

    lbl_codigo = Label(window, text="Talla:")
    lbl_codigo.grid(column=0, row=1)
    txt_codigo = Entry(window,width=10)
    txt_codigo.grid(column=1, row=1)

    lbl_email = Label(window, text="e-mail:")
    lbl_email.grid(column=0, row=2)
    txt_email = Entry(window,width=40)
    txt_email.grid(column=1, row=2)

    lbl_web_name = Label(window, text="Página:")
    lbl_web_name.grid(column=0, row=3)
    web_name = Combobox(window)
    web_name['values']= ("Supreme", "Amazon", "Adidas")
    web_name.grid(column=1, row=3)

    lbl_cardn = Label(window, text="Tarjeta de crédito:")
    lbl_cardn.grid(column=0, row=4)
    txt_cardn = Entry(window,width=40)
    txt_cardn.grid(column=1, row=4)

    lbl_codigo = Label(window, text="CVV:")
    lbl_codigo.grid(column=0, row=5)
    txt_codigo = Entry(window,width=10)
    txt_codigo.grid(column=1, row=5)

    lbl_venc = Label(window, text="Fecha vencimiento:")
    lbl_venc.grid(column=0, row=6)
    txt_venc = Entry(window,width=10)
    txt_venc.grid(column=1, row=6)

    lbl_nom = Label(window, text="Nombre completo:")
    lbl_nom.grid(column=0, row=7)
    txt_nom = Entry(window,width=40)
    txt_nom.grid(column=1, row=7)

    lbl_dir = Label(window, text="Dirección:")
    lbl_dir.grid(column=0, row=8)
    txt_dir = Entry(window,width=40)
    txt_dir.grid(column=1, row=8)

    lbl_cp = Label(window, text="C.P.:")
    lbl_cp.grid(column=0, row=9)
    txt_cp = Entry(window,width=40)
    txt_cp.grid(column=1, row=9)

    lbl_ciudad = Label(window, text="Ciudad:")
    lbl_ciudad.grid(column=0, row=10)
    txt_ciudad = Entry(window,width=40)
    txt_ciudad.grid(column=1, row=10)

    btn_compra = Button(window, text="Comprar!", command=comprar)
    btn_compra.grid(column=1, row=11)

    window.mainloop()
main()
