import telebot

import constant

bot = telebot.TeleBot(constant.token)


@bot.message_handler(content_types=["text"])
def lesson(message):
    if message.text == "пн":
        bot.send_message(message.from_user.id, "8:00: Физ-ра")
    elif message.text == 'вт':
        bot.send_message(message.from_user.id, "10:10: Алгем в 1409")
    elif message.text == "ср":
        bot.send_message(message.from_user.id, "8:30: Матан в 1509")
    elif message.text == "чт":
        bot.send_message(message.from_user.id, "11:50: Англ в 1509 + Русский в 1311")
    elif message.text == "пт":
        bot.send_message(message.from_user.id, "11:50: Англ в 1412" + " " + "14:00: Англ в 1405"+ " " + "15:40: Дискра")
    elif message.text == "сб":
        bot.send_message(message.from_user.id, "11:50: Инфа на 13 этаже ")
    elif message.text == "вскр":
        bot.send_message(message.from_user.id, "Совсем крыша поехала?")
    else:
        get_text_messages(message)


@bot.message_handler(content_types=["text"])
def mine(message):
    if message.text == "Моё" or "моё":
        bot.send_message(message.chat.id, "")
    else:
        pass


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Расписание к вашим услугам, сэр")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Этот бот создан для расписания. Напишите /start")

    elif message.text == 'Лекции':
        bot.send_message(message.from_user.id, "Введи день недели")

    elif message.text == 'Расписание' or '/tt':
        bot.send_message(message.from_user.id, "Ваше или Лекции?")

    elif message.text == "Благодарю":
        bot.send_message(message.from_user.id, "И вам всего хорошего!")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
