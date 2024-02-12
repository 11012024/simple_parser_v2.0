from threading import Thread
import telebot


# Created: Sunday, June 12, 2022, 5:23:23 PM


class TelegramBot:

    __token = '5570886380:AAHR94bnO4DD-J2dWphrJK-KQQ5jXiIeAnQ'

    def __init__(self):
        # initializing my bot
        self.__bot = telebot.TeleBot(token=TelegramBot.__token)
        # id of chat with user
        self.__chat_id = None
        # subscribing method for event.
        # When user will send '/start' command, bot will send greeting.
        self.send_greeting = self.__bot.message_handler(commands=['start'])(self.send_greeting)

    def initialize(self):
        self.__bot.polling(none_stop=True)

    """ Using for start my bot working """
    def bot_launch(self):
        # starting it in another thread
        Thread(target=self.initialize, daemon=True).start()
        # simple indicating of successful launch
        print('bot launched!')

    def send_greeting(self, message):
        self.__chat_id = message.chat.id
        greeting = f"Helllooo, dear {message.from_user.full_name}! I`m just a ducky!\nMy founder is @pleasant_user!"
        self.__bot.send_message(chat_id=self.__chat_id, text=greeting)

    def send_info(self, difference, exchange1, exchange2, pair_1, pair_2):
        if self.__chat_id is not None:
            message = f"\u2757 profit: {difference} \u2757 \n{pair_1} - {pair_2}\n" \
                  f"            {exchange1} - {exchange2}"
            self.__bot.send_message(chat_id=self.__chat_id, text=message)
        else:
            print('I have not yet written to the bot!')
