#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer


bot = ChatBot(
    'SQLMemoryTerminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

#newtrainer = UbuntuCorpusTrainer(bot)
#newtrainer.train()

trainer = ListTrainer(bot)
trainer.train([
    "Hi there!",
    "Hello",
    ])

trainer.train([
    "Greetings!",
    "Hello",
    ])

trainer.train([
    "I need help",
    "Sure, how can I help",
    "I am looking for something"
    "What is it you are looking for?",
    ])


while True:
    try:
        question = input("user input > " )
        response = bot.get_response(question)
        print("Bot > %f %s" % (response.confidence, response))

    except (KeyboardInterrupt, EOFError, SystemExit):
        break

