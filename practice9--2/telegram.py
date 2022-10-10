import telebot
import transform_num
import model_math
import mylog

bot = telebot.TeleBot('5632601232:AAE0skbOpO1ufb9rma2u-NddsPxLUZCm0iU')

button_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_start.row(telebot.types.KeyboardButton('Старт'))

button_log = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_log.row(telebot.types.KeyboardButton('Скачать лог'))

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'),
             telebot.types.KeyboardButton('Посмотреть лог'),
             telebot.types.KeyboardButton('Ещё не определился'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'),
             telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))


# @bot.message_handler(commands=['start'])
# def start_calc(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id,
#                      text='Начнем?\n',
#                      reply_markup=button_start)
#     bot.register_next_step_handler(msg, hello)


@bot.message_handler(commands=['log'])
def get_log(msg: telebot.types.Message):
    bot.send_document(chat_id=msg.from_user.id,
                      data=open('calc_bot.log', 'rb'))
    bot.send_message(chat_id=msg.from_user.id,
                     text='Выберите режим работы калькулятора\n',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)


# @bot.message_handler(content_types=['document'])
# def send_doc(msg: telebot.types.Message):
#     file = bot.get_file(msg.document.file_id)
#     downloaded_file = bot.download_file(file.file_path.log)
#     with open('calc_bot.log', 'wb') as f_out:
#         f_out.write(downloaded_file)
#         # Открываем и импортируем


@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)

    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    mylog.write_msg(msg.from_user.id, msg.text)
    if msg.text == 'Комплексные':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите действие: ',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, get_complex_do)
    elif msg.text == 'Рациональные':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите действие: ',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, get_rational_do)
    elif msg.text == 'Посмотреть лог':
        bot.send_document(chat_id=msg.from_user.id, data=open('calc_bot.log', 'rb'))
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Возвращайтесь, когда определитесь.')
    elif msg.text == '/log':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Скачать лог?',
                         reply_markup=button_log)
        bot.register_next_step_handler(msg, get_log)
    elif msg.text == '/start':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Начнем?',
                         reply_markup=button_start)
        bot.register_next_step_handler(msg, hello)
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки.')

        bot.send_message(chat_id=msg.from_user.id,
                         text='Выберите режим работы калькулятора.',
                         reply_markup=buttons1)


def get_complex_do(msg: telebot.types.Message):
    mylog.write_msg(msg.from_user.id, msg.text)
    do = msg.text
    if do in ("+", "-", "*", "/"):
        bot.register_next_step_handler(msg, get_complex_value1, do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите первое число (формат: "2+3j"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.register_next_step_handler(msg, get_complex_do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки.',
                         reply_markup=buttons2)


def get_complex_value1(msg: telebot.types.Message, do):
    mylog.write_msg(msg.from_user.id, msg.text)
    value1 = msg.text
    if transform_num.check_complex(value1) is True:
        bot.register_next_step_handler(msg, complex_counter, do, value1)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите второе число (формат: "2+3j"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.register_next_step_handler(msg, get_complex_value1, do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Неверный формат. Введите первое число (формат: "2+3j"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def complex_counter(msg: telebot.types.Message, do, value1):
    mylog.write_msg(msg.from_user.id, msg.text)
    value2 = msg.text
    if transform_num.check_complex(value2) is True:
        num1, num2 = transform_num.transform_complex(value1, value2)
        if num2 == 0 and do == '/':
            bot.register_next_step_handler(msg, complex_counter, do, value1)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Ошибка! Деление на 0. Введите второе число (формат: "2+3j"): ')
        else:
            result = model_math.calc(num1, num2, do)
            mylog.write_calc(msg.from_user.id, value1, do, value2, result)
            bot.register_next_step_handler(msg, answer)
            bot.send_message(chat_id=msg.from_user.id,
                             text=f'{value1} {do} {value2} = {result}',
                             reply_markup=buttons1)
    else:
        bot.register_next_step_handler(msg, complex_counter, do, value1)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Неверный формат. Введите второе число (формат: "2+3j"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def get_rational_do(msg: telebot.types.Message):
    mylog.write_msg(msg.from_user.id, msg.text)
    do = msg.text
    if do in ("+", "-", "*", "/"):
        bot.register_next_step_handler(msg, get_rational_value1, do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите первое число (формат: "2/3"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.register_next_step_handler(msg, get_rational_do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки.',
                         reply_markup=buttons2)


def get_rational_value1(msg: telebot.types.Message, do):
    mylog.write_msg(msg.from_user.id, msg.text)
    value1 = msg.text
    if transform_num.check_rational(value1) is True:
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите второе число (формат: "2/3"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, rational_counter, do, value1)
    else:
        bot.register_next_step_handler(msg, get_rational_value1, do)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Неверный формат. Введите первое число (формат: "2/3"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def rational_counter(msg: telebot.types.Message, do, value1):
    mylog.write_msg(msg.from_user.id, msg.text)
    value2 = msg.text
    if transform_num.check_rational(value2) is True:
        if value2 == '0/0' and do == '/':
            bot.register_next_step_handler(msg, rational_counter, do, value1)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Ошибка! Деление на 0. Введите второе число (формат: "2/3"): ')
        else:
            num1, num2 = transform_num.transform_rational(value1, value2)
            result = model_math.calc(num1, num2, do)
            mylog.write_calc(msg.from_user.id, value1, do, value2, result)
            bot.register_next_step_handler(msg, answer)
            bot.send_message(chat_id=msg.from_user.id,
                             text=f'{value1} {do} {value2} = {result}',
                             reply_markup=buttons1)
    else:
        bot.send_message(chat_id=msg.from_user.id,
                         text='Неверный формат. Введите второе число (формат: "2/3"): ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, rational_counter, do, value1)


bot.polling()
