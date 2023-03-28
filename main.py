from datetime import datetime
import requests
import telebot
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello')


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTS price: {sell_price}'
                )

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "error")
        else:
            bot.send_message(message.chat.id, "Invalid command")



    bot.polling()

if __name__ == "__main__":
    telegram_bot(token)