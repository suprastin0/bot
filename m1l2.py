import config 
import telebot
import random
print(config.token)
API_TOKEN = '6730702520:AAEoRf-23QRlvvV8hlo9ABo-uxysBLLLVhU'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands='info')
def send_info(message):
    bot.reply_to(message, """\
я пока что незаконченный бот, но мой создатель смог разобраться в теории!\
 """)

@bot.message_handler(commands='choice')
def send_choice(message):
    ch = random.choice(['Саша', 'Кирилл'])
    bot.reply_to(message, ch, """\
сегодня лох \
 """) 

bot.infinity_polling()