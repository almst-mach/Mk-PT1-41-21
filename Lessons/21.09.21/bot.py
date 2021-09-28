import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("2022090332:AAEYFSiG6oCcJ9j6j43-9Iti7Ai8KewcGlo")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['update'])
def update_message(message):
    html = urlopen("https://kurs.onliner.by")
    soup = BeautifulSoup(html)

    res = soup.find_all('p', {'class': 'value rise'})

    buy = res[0].text
    sell = res[1].text
    nb = res[2].text

    bot.send_message(message.chat.id, buy + ", " + sell + ", " + nb)

bot.polling()
