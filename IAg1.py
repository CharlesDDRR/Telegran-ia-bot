import telebot
import json
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationChain

# Obtener las llaves api en el archivo json
with open('data/data.json', 'r') as f:
    JsonData = json.load(f)

# Valido y utilizo la api del bot de telegram de la variable JsonData
bot = telebot.TeleBot(JsonData["TKey"])

# Creo una environment var para validar la api de google de la variable JsonData
os.environ["GOOGLE_API_KEY"] = JsonData["GKey"]

# Creo el modulo de leguage y especifico la version
llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro")

# Creo la memoria del modelo configurando al mismo modelo 
#para que cree un resumen de la conversacion durante la interaxion
#entre el usuario y el modelo
memoria = ConversationSummaryMemory(llm=llm)

# Configoro un chatbot con el modelo de lenguaje anterior 
#la memoria anterior y especifico que devuelva en detalle el proseso
#para detectar errores
chabot = ConversationChain(llm=llm, memory=memoria, verbose=True)

# defino una variavel que va a resivir el mensage del usuario y
#va a devolver la respuesta de la IA
def Iterccion(text):
    response = chabot.predict(input = text)
    print(response)
    return response

# defino una variavle gloval para almacenar el mensage del ususario
user_message = ""

#obtengo el mensage del usuario y le envio como parametro a la funcion
#Iterccion el mensage del ususario ara que me devuelva la respuesta eh enviarsela al usuario 
@bot.message_handler(func=lambda message: True)
def responder(message):
    global user_message
    user_message = message.text
    senf = Iterccion(user_message)
    bot.reply_to(message, senf)
    
bot.polling()
