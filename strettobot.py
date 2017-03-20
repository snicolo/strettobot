#strettobot.py

import sys
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id)

    if msg['text']=='/start':
          bot.sendMessage(chat_id, 'Come vuoi viaggiare?',
                reply_markup= ReplyKeyboardMarkup(
                    keyboard=[
                        [KeyboardButton(text="Aliscafo"), KeyboardButton(text="Caronte")]
                    ]
                ))

     #aliscafo
    if msg['text'] in ['Aliscafo', '/aliscafo', 'aliscafo']:
          bot.sendMessage(chat_id, 'Scegli la tua tratta',
                 reply_markup= ReplyKeyboardMarkup(
                     keyboard=[
                         [KeyboardButton(text="Reggio - Messina"), KeyboardButton(text="Messina - Reggio")], 
                         [KeyboardButton(text="Villa - Messina"), KeyboardButton(text="Messina - Villa")]
                         ]
                 ))
                 
    #tratte aliscafi
    if msg['text'] == 'Reggio - Messina':
          bot.sendMessage(chat_id, '\n'.join(file('aliscafo_reggio_messina.html')), parse_mode='HTML')
    elif msg['text'] == 'Messina - Reggio':
          bot.sendMessage(chat_id, '\n'.join(file('aliscafo_messina_reggio.html')), parse_mode='HTML')
    elif msg['text'] == 'Villa - Messina':
          bot.sendMessage(chat_id, '\n'.join(file('aliscafo_villa_messina.html')), parse_mode='HTML')
    elif msg['text'] == 'Messina - Villa':
          bot.sendMessage(chat_id, '\n'.join(file('aliscafo_messina_villa.html')), parse_mode='HTML')
          
     
    #caronte
    if msg['text'] in ['Caronte', '/caronte', 'caronte']:
            bot.sendMessage(chat_id, 'Scegli la compagnia',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Caronte & Tourist"), KeyboardButton(text="Bluferries")]
                                ]
                            )
                         )
    #scelta compagnia
    if msg['text']=='Caronte & Tourist':
             bot.sendMessage(chat_id, 'Scegli la tratta',
                           reply_markup= ReplyKeyboardMarkup(
                             keyboard=[
                                 [KeyboardButton(text="Villa S.G. - Messina"), KeyboardButton(text="Messina - Villa S.G.")]
              ]
          )
             )
    #tragitti per compagnia 1
    if msg['text'] in ['Messina - Villa S.G.', 'Caronte da Messina a Villa']:
           bot.sendMessage(chat_id, '\n'.join(file('caronte_messina_villa.html')), parse_mode='HTML')
    elif msg['text'] in ['Villa S.G. - Messina', 'Caronte da Villa a Messina']:
           bot.sendMessage(chat_id, '\n'.join(file('caronte_villa_messina.html')), parse_mode='HTML')
     
    if msg['text']== 'Bluferries':
           bot.sendMessage(chat_id, 'Scegli la tratta',
                           reply_markup= ReplyKeyboardMarkup(
                             keyboard=[
                                 [KeyboardButton(text="Villa S.G. - Tremestieri"), KeyboardButton(text="Tremestieri - Villa S.G.")]
              ]
          )
     )
     #tragitti compagnia 2

    if msg['text'] in ['Villa S.G. - Tremestieri', 'Caronte da Villa a Tremestieri' ]:
           bot.sendMessage(chat_id, '\n'.join(file('caronte_messina_villa.html')), parse_mode='HTML')
    elif msg['text'] in ['Trestieri. - Villa S.G.', 'Caronte da Tremestieri a Villa']:
           bot.sendMessage(chat_id, '\n'.join(file('caronte_villa_messina.html')), parse_mode='HTML')

#TOKEN 

bot = telepot.Bot('######')
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)


while 1:
    time.sleep(10)
#