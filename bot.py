import telebot

# Замените 'YOUR_BOT_TOKEN' на ваш токен, полученный от @BotFather в Telegram
TOKEN = '6693299905:AAGeUQ7oX-V2xG8tadx24jj30V1NoGAbkK8'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu Aleykum! Savol yoki murojaatingizni yozib qoldiring!")

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускаем бота
bot.polling()
