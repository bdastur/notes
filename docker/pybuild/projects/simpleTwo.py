#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
#import chatterbot.comparisons.LevenshteinDistance
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response

# A simple preprocessor.
def simplePreprocessor(statement):
    return statement

bot = ChatBot(
    'Norm',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': LevenshteinDistance,
            "response_selection_method": get_first_response
        },
        'chatterbot.logic.UnitConversion',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'simpleTwo.simplePreprocessor'
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

trainer.train([
    "What is DLM?",
    "DLM stands for Data Lifecycle Manager",
    "What is DLM?",
    "DLM is an automation framework that allows taking backup of EBS volumes"
    ])


while True:
    try:
        question = input("user input > " )
        response = bot.get_response(question)
        print("Bot > %f %s" % (response.confidence, response))

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
