import telebot
from telebot import types
bot = telebot.TeleBot('6761307593:AAHh9D7BcCo1KrPuiiBv3fHBcppUe9MWsQU')


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Salam <b><u>{message.from_user.first_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("КР Эгемендүүлүгү")
    bt2 = types.KeyboardButton("КР климаты")
    bt3 = types.KeyboardButton("КР ички аймагы")
    bt4 = types.KeyboardButton("КР жөнүндө сайтка кирүү")
    markup.add(bt1, bt2, bt3, bt4)
    bot.send_message(message.chat.id, f"Салам{message.from_user.first_name} Суроону танданыз", reply_markup=markup)

# @bot.message_handler(commands=['site'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('КР маалыматы тууралуу сайт', url='https://ky.wikipedia.org/wiki/%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD'))
#     bot.send_message(message.chat.id, 'Click it', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text=="КР климаты"):
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton("Кр табияты ж/ө маалымат сайты", url="https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D1%82%D0%B0%D0%B1%D0%B8%D1%8F%D1%82%D1%8B")
#         markup.row(btn1)
#         btn2 = types.InlineKeyboardButton("КР суулары ж/ө маалымат сайты", url="https://ky.wikipedia.org/wiki/%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD_%D0%B4%D0%B0%D1%80%D1%8B_%D1%81%D1%83%D1%83%D0%BB%D0%B0%D1%80%D1%8B")
#         btn3 = types.InlineKeyboardButton("Кр климаты ж/ө сайты", url="https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BA%D0%BB%D0%B8%D0%BC%D0%B0%D1%82%D1%8B")
#         markup.row(btn2, btn3)
#         bot.send_message(message.chat.id, text="Суроону тандан ", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text =="КР ички аймагы"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("КР шаарлары ж/ө сайты", url="https://www.google.com/search?q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D1%88%D0%B0%D0%B0%D1%80%D0%BB%D0%B0%D1%80%D1%8B&client=ubuntu-sn&hs=3xI&sca_esv=589691683&channel=fs&sxsrf=AM9HkKnzLQ4aaB3qFc1KjSFhAW5Tkm9Sog%3A1702274164074&ei=dKR2ZbOOBMmgwPAP7KWtCA&ved=0ahUKEwizmPC22YaDAxVJEBAIHexSCwEQ4dUDCBA&uact=5&oq=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D1%88%D0%B0%D0%B0%D1%80%D0%BB%D0%B0%D1%80%D1%8B&gs_lp=Egxnd3Mtd2l6LXNlcnAiK9C60YvRgNCz0YvQt9GB0YLQsNC90LTRi9C9INGI0LDQsNGA0LvQsNGA0YsyBRAAGIAEMgUQABiABEjGkAFQ2gtY1YwBcA94AZABAJgBvQOgAZ85qgELMC4yMy4xMS4xLjG4AQPIAQD4AQGoAhPCAgcQIxjqAhgnwgIQEAAYAxiPARjqAhi0AtgBAcICEBAuGAMYjwEY6gIYtALYAQHCAgsQLhiABBixAxiDAcICCxAAGIAEGLEDGIMBwgIEEAAYA8ICCBAAGIAEGLEDwgIOEAAYgAQYigUYsQMYgwHCAhoQLhiABBixAxiDARiXBRjcBBjeBBjgBNgBAsICBRAuGIAEwgILEC4YARiABBgKGCrCAgkQABgBGIAEGArCAg8QLhgBGIAEGMcBGNEDGArCAg8QLhgBGIAEGMcBGK8BGArCAhoQLhgBGIAEGAoYKhiXBRjcBBjeBBjgBNgBAsICCRAuGAEYgAQYCsICDRAuGIAEGMcBGK8BGArCAgwQLhgeGMcBGK8BGArCAgkQABgeGPEEGArCAgcQIxixAhgnwgIKEC4YgAQYsQMYCsICChAAGIAEGLEDGArCAgoQABiABBiKBRhDwgINEC4YgAQYsQMYgwEYCsICDRAAGIAEGLEDGIMBGArCAgcQIxiuAhgnwgIHEAAYgAQYAcICBxAjGLACGCfCAgcQABiABBgNwgIKECMYgAQYigUYJ8ICDRAuGIAEGIoFGEMYsQPCAgoQLhiABBiKBRhDwgIOEC4YgAQYigUYsQMYgwHCAggQLhiABBixA8ICBhAAGBYYHuIDBBgAIEGIBgG6BgYIARABGAq6BgYIAhABGBQ&sclient=gws-wiz-serp")
        btn2 = types.InlineKeyboardButton("КР облустары ж/ө сайты", url="https://www.google.com/search?q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BE%D0%B1%D0%BB%D1%83%D1%81%D1%82%D0%B0%D1%80%D1%8B&client=ubuntu-sn&sca_esv=589691683&channel=fs&sxsrf=AM9HkKnXBRmI8rncDjhC9JhuOdhBKqIrLA%3A1702275069446&ei=_ad2ZbToGrz8wPAP6di8uAU&ved=0ahUKEwj02svm3IaDAxU8PhAIHWksD1cQ4dUDCBA&uact=5&oq=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BE%D0%B1%D0%BB%D1%83%D1%81%D1%82%D0%B0%D1%80%D1%8B&gs_lp=Egxnd3Mtd2l6LXNlcnAiLdC60YvRgNCz0YvQt9GB0YLQsNC90LTRi9C9INC-0LHQu9GD0YHRgtCw0YDRizIFEAAYgAQyBRAAGIAESNJYUPsWWMFScAF4AZABAJgBjgKgAeQjqgEHMC4xMy4xMLgBA8gBAPgBAagCFMICBxAjGOoCGCfCAhMQABiABBiKBRhDGOoCGLQC2AEBwgIUEAAYgAQY4wQY6QQY6gIYtALYAQHCAhAQABgDGI8BGOoCGLQC2AECwgIKECMYgAQYigUYJ8ICChAAGIAEGIoFGEPCAg0QLhiABBiKBRhDGLEDwgILEC4YgAQYxwEYrwHCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIIEC4YgAQYsQPCAgsQLhiABBixAxiDAcICBhAAGBYYHuIDBBgAIEGIBgG6BgYIARABGAG6BgYIAhABGAo&sclient=gws-wiz-serp")
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton("КР райондору ж/ө сайты", url="https://www.google.com/search?q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BE%D0%B1%D0%BB%D1%83%D1%81%D1%82%D0%B0%D1%80%D1%8B&client=ubuntu-sn&sca_esv=589691683&channel=fs&sxsrf=AM9HkKnXBRmI8rncDjhC9JhuOdhBKqIrLA%3A1702275069446&ei=_ad2ZbToGrz8wPAP6di8uAU&ved=0ahUKEwj02svm3IaDAxU8PhAIHWksD1cQ4dUDCBA&uact=5&oq=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BE%D0%B1%D0%BB%D1%83%D1%81%D1%82%D0%B0%D1%80%D1%8B&gs_lp=Egxnd3Mtd2l6LXNlcnAiLdC60YvRgNCz0YvQt9GB0YLQsNC90LTRi9C9INC-0LHQu9GD0YHRgtCw0YDRizIFEAAYgAQyBRAAGIAESNJYUPsWWMFScAF4AZABAJgBjgKgAeQjqgEHMC4xMy4xMLgBA8gBAPgBAagCFMICBxAjGOoCGCfCAhMQABiABBiKBRhDGOoCGLQC2AEBwgIUEAAYgAQY4wQY6QQY6gIYtALYAQHCAhAQABgDGI8BGOoCGLQC2AECwgIKECMYgAQYigUYJ8ICChAAGIAEGIoFGEPCAg0QLhiABBiKBRhDGLEDwgILEC4YgAQYxwEYrwHCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIIEC4YgAQYsQPCAgsQLhiABBixAxiDAcICBhAAGBYYHuIDBBgAIEGIBgG6BgYIARABGAG6BgYIAhABGAo&sclient=gws-wiz-serp")
        btn4 = types.InlineKeyboardButton("КР айылдары ж/ө сайты", url="https://www.google.com/search?q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%B0%D0%B9%D1%8B%D0%BB%D0%B4%D0%B0%D1%80%D1%8B&client=ubuntu-sn&sca_esv=589691683&channel=fs&sxsrf=AM9HkKkTrGI374kK62I2eAttpIJS6uHoeA%3A1702275139163&ei=Q6h2ZYnGCf6ywPAPz9ejgAk&ved=0ahUKEwjJ8-qH3YaDAxV-GRAIHc_rCJAQ4dUDCBA&uact=5&oq=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%B0%D0%B9%D1%8B%D0%BB%D0%B4%D0%B0%D1%80%D1%8B&gs_lp=Egxnd3Mtd2l6LXNlcnAiK9C60YvRgNCz0YvQt9GB0YLQsNC90LTRi9C9INCw0LnRi9C70LTQsNGA0YsyBRAAGIAESLE5UJEEWL4tcAJ4AZABAJgB6QGgAZQaqgEGMC4xMy41uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAgoQIxiABBiKBRgnwgIKEAAYgAQYigUYQ8ICBhAAGBYYHsICBxAAGIAEGA3iAwQYACBBiAYBkAYK&sclient=gws-wiz-serp")
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, text="Сайтты тандаңыз", reply_markup=markup)

    elif (message.text == "КР климаты"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("КР табияты ж/ө маалымат сайты",
                                          url="https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D1%82%D0%B0%D0%B1%D0%B8%D1%8F%D1%82%D1%8B")
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton("КР суулары ж/ө маалымат сайты",
                                          url="https://ky.wikipedia.org/wiki/%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD_%D0%B4%D0%B0%D1%80%D1%8B_%D1%81%D1%83%D1%83%D0%BB%D0%B0%D1%80%D1%8B")
        btn3 = types.InlineKeyboardButton("КР климаты ж/ө сайты",
                                          url="https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%D0%BA%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D1%8B%D0%BD+%D0%BA%D0%BB%D0%B8%D0%BC%D0%B0%D1%82%D1%8B")
        markup.row(btn2, btn3)
        bot.send_message(message.chat.id, text="Сайтты тандаңыз ", reply_markup=markup)

    elif(message.text=="КР жөнүндө сайтка кирүү"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('КР тууралуу маалымат', url='https://ky.wikipedia.org/wiki/%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD'))
        bot.send_message(message.chat.id, 'Click its', reply_markup=markup)
    elif(message.text=="КР Эгемендүүлүгү"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("КР эгемендүүлүгү,гимни")
        btn2 = types.KeyboardButton("КР герби, желеги")
        btn3 = types.KeyboardButton("КР Дини")
        btn4 = types.KeyboardButton("КР калкы,чек арасы, акчалай бирдиги")
        btn5 = types.KeyboardButton("КР конституциясы, тили")
        btn6 = types.KeyboardButton("Башкы менюга кайтуу")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text='Суроону тандаңыз', reply_markup=markup)
    elif(message.text=="КР эгемендүүлүгү,гимни"):
        bot.send_message(message.chat.id, text="1991-жылдын 31-августунда Кыргызстандын тарыхында жаңы барак ачылган – Кыргыз мамлекетинин көз карандысыздыгы жана эгемендүүлүгү жарыяланган,1992-жылы 18-декабрда Кыргыз Республикасынын Жогорку Кеңештин № 1141-XII токтому менен бекитилген.Сөзүн Жалил Садыков, Шабданбек Кулуев, музыкасын Насыр Давлесов менен Калый Молдобасанов жазган. ")
    elif(message.text=="КР герби, желеги"):
        bot.send_message(message.chat.id, text="Туу Кыргызстан Республикасынын Жогорку Советинин 1992-жылдын 3-мартындагы токтому менен бекитилген."
                                               "Авторлору:Э. Айдарбеков,Б. Жайчыбеков, С. Иптаров, Ж. Матаев, М. Сыдыков."
                                               "Герб Кыргыз Республикасынын Жогорку Кеңешинин 1994-жылдын 14-январындагы токтому менен бекитилген.Авторлору: А. Абдраев и С. Дубанаев")
    elif(message.text=="КР Дини"):
        bot.send_message(message.chat.id, text="Калктын 75%ы ислам динин жана 20%ы православие динин кармануу аркылуу рухий байлыктарга жетишет. Жарандардын 5 %ы гана башка диндердин үлүшүнө туура келет."
                                               "Диндери – динге ишенүүчүлөдүн көбү– мусулмандар. Христиандар да бар: православдар, католиктер жана протестанттар (лютерандар, баптисттер, адвентисттер).")
    elif(message.text=="КР калкы,чек арасы, акчалай бирдиги"):
        bot.send_message(message.chat.id, text="Кыргызстан Орто Азиядан орун алган. Ал Казакстан, Кытай, Тажикстан, Өзбекстан менен чектешет.Кыргызстандын калкы 7 миллионго жетти.Калктын көпчүлүгү республиканын түштүгүндө"
                                               " — Ош, Жалал-Абад, Баткен облустарында жана Ош шаарында (3,4 млн. адам же республиканын калкынын 53%), алардын көпчүлүгү Фергана өрөөнүнүн кыргыз бөлүгүндө жашашат."
                                               " Ошондой эле, калктын кыйла үлүшү Чүй өрөөнүндө (Чүй облусу жана Бишкек шаары; 1,9 млн. адам же республика калкынын 31%) топтолгон. Эң жыш жайгашкан облустар (республикалык маанидеги шаарлардын калкын кошо алганда) Ош жана Чүй.""Сом — Кыргызстандын акча бирдиги.Улуттук валютанын бардык банкноттору жана монеталары Кыргыз Республикасынын аймагында"
                                               " расмий төлөм каражаты статусуна ээ жана кайсы жылы чыгарылгандыгына карабастан, төлөм каражаты катары төлөөгө милдеттүү түрдө кабыл алынууга тийиш.Кыргыз Республикасынын улуттук акча бирдиги сом өлкө эгемендүүлүк алгандан кийин, 1993-жылы 10-майда жүгүртүүгө чыгарылган")
    elif(message.text=="КР конституциясы, тили"):
        bot.send_message(message.chat.id, text="1993-жылдын 5-майында өлкөнүн жаңы Конституциясы кабыл алынган.Мамлекеттик тил — кыргыз тили, орус тили расмий статуска ээ. 2009-жылдагы эл каттоонун маалыматы боюнча, 4,1 миллион адам үчүн кыргыз тили — эне тили же экинчи тил, ал эми 2,5 миллион адам үчүн орус тили — эне тили же экинчи тил. Орус тили — эң кеңири колдонулган экинчи тил, андан кийин кыргыз, өзбек жана англис тилдери.")
    elif(message.text=="Башкы менюга кайтуу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("КР Эгемендүүлүгү")
        bt2 = types.KeyboardButton("КР климаты")
        bt3 = types.KeyboardButton("КР ички аймагы")
        markup.add(bt1, bt2, bt3)
        bot.send_message(message.chat.id, text="Сиз башкы менюдасыз", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Команда туура эмес")

# @bot.message_handler(content_types=['site'])
# def website(message):


bot.polling(none_stop=True)