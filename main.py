import telebot
from telebot import types

# 1242746587:AAEudORvza69QRomJTG2Rmudk5J857xJAjI
bot = telebot.TeleBot("1242746587:AAEudORvza69QRomJTG2Rmudk5J857xJAjI")
name = ''
surname = ''
age = 0


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Ну здорова бандит')
    elif message.text == 'Привет!':
        bot.reply_to(message, 'Ну здорова, я смотрю ты пунктуацию любишь.')
    elif message.text == 'привет!':
        bot.reply_to(message, 'Заглавная буква П для тебя шутка что-ли?')
    elif message.text == 'привет':
        bot.reply_to(message, 'Заглавная буква П для тебя шутка что-ли?')
    elif message.text == 'hi':
        bot.reply_to(message, 'Не брат ты мне, чушка...')
    elif message.text == 'Помощь':
        bot.reply_to(message, 'Здравствуйте!\nВы можете использовать такие команды как:\nПривет\nПривет!\nпривет!\nпривет\nhi\nРегистрация')
    elif message.text == 'Регистрация':
        bot.send_message(message.from_user.id, "Ну давай познакомимся, че. Как звать?")
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'А фамилию назовешь, если есть?')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, name + ', а че по возрасту?')
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Не, ты думаешь что я дебил? Пиши цифрами лошара.")
        break
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Допустим', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Я дэбил', callback_data='no')
    keyboard.add(key_no)
    question = "Слышь, домовенок, тебе " + str(age) + ' лет? Или ты дурачок, который не знает сколько тебе лет..'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Ну ладно, прощу тебя и возьму в расчет.")
    if call.data == 'no':
        bot.send_message(call.message.chat.id, "И как с таким дятелом работать? Давай еще раз...")
        bot.send_message(call.from_user.id, "Ну давай познакомимся, че. Как звать?")
        bot.register_next_step_handler(call.message, reg_name)


bot.polling()
