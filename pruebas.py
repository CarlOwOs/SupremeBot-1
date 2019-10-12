import bot as bot

def main():
    C = bot.Compra("Delta Logo Varsity Jacket", "S", "megaelius4@gmail.com", "Supreme",
                   "0000 1111 2222 3333", "123", "01/20", "Pepito Pérez",
                   "Calle arriba 1", "03300", "Orihuela")
    bot.Busca_producto(C)
main()
