from tkinter import *
from tkinter.ttk import *
import bot as bot
'''
def guardar():
    datos = txt_prod.get()+";"+txt_talla.get()+";"+txt_email.get()+";"+box_web_name.get()+";"+txt_cardn.get()+";"+txt_codigo.get()+";"+txt_venc.get()+";"+txt_nom.get()+";"+txt_dir.get()+";"+txt_cp.get()+";"+txt_ciudad.get(),+";"+txt_tel.get()
    fd = open("preset.txt")
    write(fd,datos)
    fd.close()
'''
def cargar():
    datos = open("preset.txt").read().split(';')
    print(datos)
    Compra = bot.Compra(datos[0],datos[1],datos[2],datos[3],datos[4],
                        datos[5],datos[6],datos[7],datos[8],datos[9],
                        datos[10],datos[11].rstrip())
    bot.dinerito(Compra)

def comprar():
    Compra = bot.Compra(txt_prod.get(), txt_talla.get(), txt_email.get(),
                        box_web_name.get(), txt_cardn.get(), txt_codigo.get(),
                        txt_venc.get(), txt_nom.get(), txt_dir.get(), txt_cp.get(),
                        txt_ciudad.get(), txt_tel.get())
    bot.dinerito(Compra)


window = Tk()
window.title("SupremeBot")
window.geometry('400x400')
lbl_prod = Label(window, text="Nombre del producto:")
lbl_prod.grid(column=0, row=0)
txt_prod = Entry(window,width=40)
txt_prod.grid(column=1, row=0)

lbl_talla = Label(window, text="Talla:")
lbl_talla.grid(column=0, row=1)
txt_talla = Entry(window,width=10)
txt_talla.grid(column=1, row=1)

lbl_email = Label(window, text="e-mail:")
lbl_email.grid(column=0, row=2)
txt_email = Entry(window,width=40)
txt_email.grid(column=1, row=2)

lbl_web_name = Label(window, text="Página:")
lbl_web_name.grid(column=0, row=3)
box_web_name = Combobox(window)
box_web_name['values']= ("Supreme", "Amazon", "Adidas")
box_web_name.grid(column=1, row=3)

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

lbl_tel = Label(window, text="Teléfono:")
lbl_tel.grid(column=0, row=11)
txt_tel = Entry(window,width=40)
txt_tel.grid(column=1, row=11)

btn_carga = Button(window, text="Cargar y comprar", command=cargar)
btn_carga.grid(column=0, row=12)

btn_compra = Button(window, text="Comprar!", command=comprar)
btn_compra.grid(column=1, row=12)

btn_guardar = Button(window, text="Guardar preset", command=guardar)
btn_guardar.grid(column=0, row=13)

window.mainloop()
