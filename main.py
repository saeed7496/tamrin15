
from numpy import argmax
import qrcode
import telebot
import random
saeed_bot = telebot.TeleBot('5322435564:AAHixEYn5_pbk2vcOFy0V7OaYnr6fUngGSI') 

murk=telebot.types.ReplyKeyboardMarkup()
btn=telebot.types.KeyboardButton('new game')
murk.add(btn)


@saeed_bot.message_handler(commands=['start'])
def send_wellcom(message):
    saeed_bot.reply_to(message,f'سلام{message.chat.first_name}خوش اومدی...')


@saeed_bot.message_handler(commands=['game'])
def game(message):
    saeed_bot.reply_to(message,'یک عدد بین 0 تا 100 حدس بزن\n برو بریم')
    global adad
    adad=random.randint(0,100)
    saeed_bot.register_next_step_handler(message,game2)
def game2(message):
    if int(message.text)>adad:
        pm=saeed_bot.reply_to(message,'کمترش کن')
        saeed_bot.register_next_step_handler(pm,game2)
    elif int(message.text)<adad:
        pm=saeed_bot.reply_to(message,'بیشترش کن')
        saeed_bot.register_next_step_handler(pm,game2)
    elif int(message.text)==adad:
        saeed_bot.reply_to(message,'آفرین درست حدس زدی...',reply_markup=murk)
        saeed_bot.register_next_step_handler(message,game)


@saeed_bot.message_handler(commands=['max'])
def max1(message):
    saeed_bot.reply_to(message,'اعداد رو وارد کن و بین شون "," بذار')
    saeed_bot.register_next_step_handler(message,max2)
def max2(message):
    data=str(message.text)
    l=data.split(',')
    lst=[int(i) for i in l]
    saeed_bot.send_message(message.chat.id,'maximum is: '+str(max(lst)))


@saeed_bot.message_handler(commands=['argmax'])
def arg_max1(message):
    saeed_bot.reply_to(message,'اعداد رو وارد کن و بین شون "," بذار')
    saeed_bot.register_next_step_handler(message,arg_max2)
def arg_max2(message):
    data=str(message.text)
    l=data.split(',')
    lst=[int(i) for i in l]
    saeed_bot.send_message(message.chat.id,'argmax is: '+str(argmax(lst)+1))


@saeed_bot.message_handler(commands=['qrcode'])
def qr1(message):
    saeed_bot.reply_to(message,'متنی که میخای کد کیو آر واسش بسازم رو به صورت انگلیسی وارد کن')
    saeed_bot.register_next_step_handler(message,qr2)
def qr2(message):
    text=message.text
    image=qrcode.make(text)
    image.save('qr.png')
    file=open('qr.png','rb')
    saeed_bot.send_photo(message.chat.id,file)


@saeed_bot.message_handler(commands=['help'])
def help(message):
    saeed_bot.reply_to(message,'کارهایی ک میتونم انجام بدم رو به صورت عکس برات میفرستم')
    file=open('photo.jpg','rb')
    saeed_bot.send_photo(message.chat.id,file)

saeed_bot.polling()