from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7012019536:AAFTGSaGEcbW4oppI2TjBXsuOv9PaR7gFhI')



@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    print(chat_id)
    bot.send_message(chat_id, f"Assalomu alaykum {full_name}")


@bot.message_handler(content_types=["text", "photo"])
def get_text(message: Message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, text)
    # bot.copy_message(-4184520416, chat_id, message.message_id)



bot.polling()


""" echo "# tele_bot" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ABDUMAJIDOVAA/tele_bot.git
git push -u origin main """