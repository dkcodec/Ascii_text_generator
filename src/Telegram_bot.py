from telebot import types
import Ascii_generator
import telebot
import key

bot = telebot.TeleBot(key.BOT_TOKEN)
available_commands = ['/start', '/fonts', '/commands']
font_name = 'banner'

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Say hello")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Hello! I'm ascii text generator on python!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "👋 Say hello")
def say_hello(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id, f'Okay, welcome to ASCII text generator!\nFor generating ASCII text just type the message to generate ASCII text\nIf you want to choose font, pls write /fonts (my recommendations: doh)\nFor all commands write /commands\n\nWARNING! Bot understand only English!\n```{Ascii_generator.transfer("LOL","smisome1")}```', parse_mode='Markdown',reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/commands")
    markup.add(btn1)


@bot.message_handler(commands=['fonts'])
def fonts_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for font in Ascii_generator.fonts():
        markup.add(types.KeyboardButton(f"/{font}"))
    bot.send_message(message.from_user.id, 'Choose a font:', reply_markup=markup)

@bot.message_handler(commands=Ascii_generator.fonts())
def display_font(message):
    global font_name
    font_name= message.text[1:]
    bot.send_message(message.from_user.id, 'Selected font: ' + font_name)

@bot.message_handler(commands=['commands'])
def show_commands(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for command in available_commands:
        markup.add(types.KeyboardButton(command))
    bot.send_message(message.chat.id, "Select command:", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text_message(message):

    mes = message.text

    if mes == "/":
        bot.send_message(message.chat.id, 'Take my congrats, you found easter egg ^-^')
    else:
        try:
            bot.send_message(message.chat.id, f'```\n{Ascii_generator.transfer(mes, font_name)}\n```', parse_mode='Markdown')
        except:
            bot.send_message(message.chat.id, f'Something went wrong! do not use this(these) symbol(s)',parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)