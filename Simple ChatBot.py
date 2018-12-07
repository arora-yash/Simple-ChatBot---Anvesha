from chatterbot import ChatBot
bot = ChatBot('Anvesha')

from chatterbot.trainers import ListTrainer

bot.set_trainer(ListTrainer)
#Training
bot.train(['What is your name?','My name is Anvesha'])
bot.train(['Who are you?','I am a bot, created by you.'])
bot.train(['Do you know me?','Yes, you created me.','Yash?','No Idea!!'])

import os
for files in os.listdir('./english/'):
    data=open('./english/'+files,'r').readlines()
    bot.train(data)

'''
    #Training the bot who doesn't have the upper english folder in the local computer
    
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
'''

while True:
    message = input('\t\t\tYou:')
    if message.strip()!='Bye':
        reply = bot.get_response(message)
        print('\t\t\tAnvesha: ',reply)
    if message.strip()=='Bye':
        print('Anvesha: Bye')
        break
