import telebot
from telebot import types
import psycopg2

bot = telebot.TeleBot('2122953569:AAGD7WzholCsxEE0gyw-pxZ8pJWyIGRGzoM')


def execute_read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/ponedelnik')
    btn2 = types.KeyboardButton('/vtornik')
    btn3 = types.KeyboardButton('/sreda')
    btn4 = types.KeyboardButton('/chetverg')
    btn5 = types.KeyboardButton('/pyatnica')
    btn6 = types.KeyboardButton('/subbota')
    btn7 = types.KeyboardButton('/voskresenie')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    bot.send_message(message.chat.id, 'Выберите день недели', reply_markup=markup)


@bot.message_handler(commands=['ponedelnik'])
def pon(message):
    conn = psycopg2.connect(database="tb", user="postgres", password="1", host="localhost", port="5432")
    text = "select tb.timetable.subject, tb.timetable.room_numb, tb.timetable.start_time, tb.teacher.full_name from tb.timetable "\
           "join tb.teacher on tb.timetable.subject = tb.teacher.subject where day = 'Pon'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, 'Ponedelnik:')
    for row in subjects:
        stroka = ''
        stroka = row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3]
        bot.send_message(message.chat.id, stroka)


@bot.message_handler(commands=['vtornik'])
def vto(message):
    conn = psycopg2.connect(database="tb", user="postgres", password="1", host="localhost", port="5432")
    text = "select tb.timetable.subject, tb.timetable.room_numb, tb.timetable.start_time, tb.teacher.full_name from tb.timetable "\
           "join tb.teacher on tb.timetable.subject = tb.teacher.subject where day = 'Vtor'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, 'Vtornik:')
    for row in subjects:
        stroka = ''
        stroka = row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3]
        bot.send_message(message.chat.id,  stroka)


@bot.message_handler(commands=['sreda'])
def sre(message):
    conn = psycopg2.connect(database="tb", user="postgres", password="1", host="localhost", port="5432")
    text = "select tb.timetable.subject, tb.timetable.room_numb, tb.timetable.start_time, tb.teacher.full_name from tb.timetable "\
           "join tb.teacher on tb.timetable.subject = tb.teacher.subject where day = 'Sred'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, 'Sreda:')
    for row in subjects:
        stroka = ''
        stroka = row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3]
        bot.send_message(message.chat.id, stroka)


@bot.message_handler(commands=['chetverg'])
def che(message):
    conn = psycopg2.connect(database="tb", user="postgres", password="1", host="localhost", port="5432")
    text = "select tb.timetable.subject, tb.timetable.room_numb, tb.timetable.start_time, tb.teacher.full_name from tb.timetable " \
           "join tb.teacher on tb.timetable.subject = tb.teacher.subject where day = 'Chet'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, 'Chetverg:')
    for row in subjects:
        stroka = ''
        stroka = row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3]
        bot.send_message(message.chat.id, stroka)


@bot.message_handler(commands=['pyatnica'])
def pya(message):
    conn = psycopg2.connect(database="tb", user="postgres", password="1", host="localhost", port="5432")
    text = "select tb.timetable.subject, tb.timetable.room_numb, tb.timetable.start_time, tb.teacher.full_name from tb.timetable "\
           "join tb.teacher on tb.timetable.subject = tb.teacher.subject where day = 'Pyat'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, 'Pyatnica:')
    for row in subjects:
        stroka = ''
        stroka = row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3]
        bot.send_message(message.chat.id, stroka)


@bot.message_handler(commands=['subbota'])
def sub(message):
    bot.send_message(message.chat.id, 'Subbota: не учебный день')


@bot.message_handler(commands=['voskresenie'])
def vos(message):
    bot.send_message(message.chat.id, 'Voskresenie: не учебный день')

bot.infinity_polling()

