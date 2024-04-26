#!! para ejecutar este proyecto deve poner su api de google IA en la variavle
# Gkey del archivo json y la api de su bot de telegram en la variavle Tkey del mismo archivo json

# Importo desde el script IAg1.py los modulos, variavles, funciones y 
# tecnologias necesarias 
import IAg1

@bot.message_handler(func=lambda message: True)
def responder(message):
    global user_message
    user_message = message.text
    senf = Iterccion(user_message)
    bot.reply_to(message, senf)

bot.polling()
