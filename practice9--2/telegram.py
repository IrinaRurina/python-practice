import telebot
import transform_num
import model_math

bot = telebot.TeleBot('xxx')

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'),
             telebot.types.KeyboardButton('Ещё не определился'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'),
             telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))

# @bot.message_handler(commands=['log'])
# def log(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id,
#                      text='Лог программы.......',
#                      reply_markup=buttons)
#     bot.register_next_step_handler(msg, answer)


@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)

    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите действие: ',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, get_complex_value1)
    elif msg.text == 'Рациональные':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите действие: ',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, get_rational_value1)
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons1)


def get_complex_value1(msg: telebot.types.Message):
    do = msg.text
    bot.register_next_step_handler(msg, get_complex_value2, do)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите первое число (формат: "2+3j"): ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def get_complex_value2(msg: telebot.types.Message, do):
    value1 = msg.text
    bot.register_next_step_handler(msg, complex_counter, do, value1)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите второе число (формат: "2+3j"): ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def get_rational_value1(msg: telebot.types.Message):
    do = msg.text
    bot.register_next_step_handler(msg, get_rational_value2, do)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите второе число (формат: "2/3"): ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def get_rational_value2(msg: telebot.types.Message, do):
    value1 = msg.text
    bot.register_next_step_handler(msg, rational_counter, do, value1)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите второе число (формат: "2/3"): ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def complex_counter(msg: telebot.types.Message, do, value1):
    value2 = msg.text
    print(do)
    print(value1)
    print(value2)
    num1, num2 = transform_num.transform_complex(value1, value2)
    result = model_math.calc(num1, num2, do)
    bot.register_next_step_handler(msg, hello)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'{value1} {do}, {value2} = {result}',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def rational_counter(msg: telebot.types.Message, do, value1):
    value2 = msg.text
    num1, num2 = transform_num.transform_rational(value1, value2)
    result = model_math.calc(num1, num2, do)
    bot.register_next_step_handler(msg, hello)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'{value1} {do}, {value2} = {result}',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


bot.polling()
