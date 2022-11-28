import telebot
import texts
import config
import extentions

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def bot_hello(message: telebot.types.Message):
    bot.send_message(message.chat.id, texts.hello)


@bot.message_handler(commands=['values'])
def bot_hello(message: telebot.types.Message):
    result = extentions.GetExchange.print_support_currency()
    bot.send_message(message.chat.id, result)


@bot.message_handler(content_types=['text', ])
def bot_convert(message: telebot.types.Message):
    result = extentions.GetExchange.get_currency_names(message.text)
    bot.send_message(message.chat.id, result)


print('-- Bot is online --')
bot.polling(none_stop=True)

