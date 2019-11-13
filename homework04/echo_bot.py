import telebot


access_token = "970813778:AAE6Ntw0p055TeNo3NHfWbs0N2vzVRptvy8"
telebot.apihelper.proxy = {'https': 'https://35.245.208.185:3128'}

bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling()

