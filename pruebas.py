import bot as bot

def main():
    C = bot.Compra("Marrakech L/S Top", "S", "megaelius4@gmail.com", "Supreme",
                   "0000 1111 2222 3333", "123", "01/20", "Pepito Pérez",
                   "Calle arriba 1", "03300", "Orihuela")
    print(bot.Busca_url_producto(C))
main()
