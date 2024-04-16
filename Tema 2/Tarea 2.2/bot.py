import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen un saludo
saludar = re.compile(r"hello|hi|hey|hola|yo", re.IGNORECASE)

# Expresión regular para detectar para otro saludo
saludo2 = re.compile(r"si, ¿que hay de ti?", re.IGNORECASE)

# Expresión regular para el juego
juego_favorito = re.compile(r"¿cu[a|á]l es tu juego favorito?|¿qu[e|é] juego te gusta?", re.IGNORECASE)
personaje_favorito = re.compile(r"¿waifu favorita?", re.IGNORECASE)
interaccion1 = re.compile(r"Wow, el m[i|í]o tambi[e|é]n", re.IGNORECASE)
interaccion2 = re.compile(r"Wow, a m[i|í] tambi[e|é]n me gusta", re.IGNORECASE)
# Expresión regular para la fecha
evento = re.compile(r"Ahora...", re.IGNORECASE)
respuesta = re.compile(r"^([a-zA-Z]?\s?)+(26)+([a-zA-Zñ]?\s?)+(abril)+([a-zA-Zñ]?\s?)+(2023)$", re.IGNORECASE)

# Expresión regular fin de charla
despedida = re.compile(r"nos vemos|adios|matane", re.IGNORECASE)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    
    if saludar.search(message_text):
        await update.message.reply_text("Hey, ¿todo bien?")
    elif saludo2.search(message_text):
        await update.message.reply_text("Es un buen día. Gracias, bro")
    elif juego_favorito.search(message_text):
        await update.message.reply_text("El mejor que he conocido y del que vengo: Honkai Star Rail")
    elif interaccion1.search(message_text):
        await update.message.reply_text("¿En serio? ¡Increíble!")
    elif personaje_favorito.search(message_text):
        await update.message.reply_text("Fácil. Mommy Kafka")
    elif interaccion2.search(message_text):
        await update.message.reply_text("¡Wow!")
    elif evento.search(message_text):
        await update.message.reply_text("Preguntas mucho, hermano. Ahora es mi turno. Parecieras conocer muy bien el juego: ¿en qué año salió?")
    elif respuesta.search(message_text):
        await update.message.reply_text("seikai")
    elif despedida.search(message_text):
        await update.message.reply_text("Hasta luego, bro")
    else:
        await update.message.reply_text("Creo que debes aprender a escribir, XD")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7184531125:AAEUHvYj291sODmP8vRiktil5_ni1-39wpQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()