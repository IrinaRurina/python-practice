import telebot
import contact_view
import contact_add
import export_pb
import import_pb


bot = telebot.TeleBot('5632601232:AAHHZTPL_I_0mcjoPbP1WHpBk62-CzDvybQ')

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Посмотреть'),
             telebot.types.KeyboardButton('Добавить'))
buttons1.row(telebot.types.KeyboardButton('Экспорт'),
             telebot.types.KeyboardButton('Импорт'))
buttons1.row(telebot.types.KeyboardButton('Еще не определился'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('Да'),
             telebot.types.KeyboardButton('Нет'))


@ bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Привет, это телефонный справочник. Что будем делать с контактами?',
                     reply_markup=buttons1)

    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):

    if msg.text == 'Посмотреть':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите букву алфавита, начальные буквы фамилии или фамилию полностью: ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, contact_search)
    elif msg.text == 'Добавить':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите Имя: ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, get_name)
    elif msg.text == 'Экспорт':
        export_pb.export_contacts()
        bot.send_document(chat_id=msg.from_user.id, data=open('my_contacts.txt', 'rb'))
        bot.send_message(chat_id=msg.from_user.id,
                         text='Что будем делать с контактами?',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    elif msg.text == 'Импорт':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Загрузите ваш файл с контактами ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, import_contacts)
    elif msg.text == 'Еще не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Возвращайтесь, когда определитесь')
        bot.register_next_step_handler(msg, hello)
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки')


@bot.message_handler(content_types=['document'])
def import_contacts(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open('new_contact_list.txt', 'wb') as f_out:
        f_out.write(downloaded_file)
    import_pb.import_contacts()
    bot.send_message(chat_id=msg.from_user.id,
                     text='Список контактов обновлен',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(chat_id=msg.from_user.id,
                     text='Что будем делать с контактами?',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)


def contact_search(msg: telebot.types.Message):
    find = msg.text
    find_list, count = contact_view.contact_search_by_surname(find)
    if count == 0:
        bot.send_message(chat_id=msg.from_user.id,
                         text='По вашему запросу контакты не найдены. Поищем еще раз?',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, contact_reply)
    else:
        for i in range(len(find_list)):
            print_contact = " ".join(find_list[i])
            bot.send_message(chat_id=msg.from_user.id,
                             text=print_contact,
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(chat_id=msg.from_user.id,
                         text='Поищем еще раз?',
                         reply_markup=buttons2)
        bot.register_next_step_handler(msg, contact_reply)


def contact_reply(msg: telebot.types.Message):
    if msg.text == 'Да':
        bot.register_next_step_handler(msg, contact_search)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите букву алфавита, начальные буквы фамилии или фамилию полностью: ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif msg.text == 'Нет':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Что будем делать с контактами?',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    else:
        bot.register_next_step_handler(msg, contact_reply)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки')


def get_name(msg: telebot.types.Message):
    name = msg.text
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите Фамилию: ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_surname, name)


def get_surname(msg: telebot.types.Message, name):
    surname = msg.text
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите Телефон: ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_phone, name, surname)


def get_phone(msg: telebot.types.Message, name, surname):
    phone = msg.text
    bot.send_message(chat_id=msg.from_user.id,
                     text='Введите комментарий: ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_comment, name, surname, phone)


def get_comment(msg: telebot.types.Message, name, surname, phone):
    comment = msg.text
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Вы ввели : {name} {surname} {phone} {comment} ',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(chat_id=msg.from_user.id,
                     text='Точно добавляем?',
                     reply_markup=buttons2)
    bot.register_next_step_handler(msg, confirm_add, name, surname, phone, comment)


def confirm_add(msg: telebot.types.Message, name, surname, phone, comment):
    if msg.text == 'Да':
        contact_add.add_new_contact(name, surname, phone, comment)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Новый контакт добавлен ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(chat_id=msg.from_user.id,
                         text='Что будем делать с контактами?',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    elif msg.text == 'Нет':
        bot.send_message(chat_id=msg.from_user.id,
                         text='Что будем делать с контактами?',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    else:
        bot.register_next_step_handler(msg, confirm_add, name, surname, phone, comment)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки')


bot.polling()
