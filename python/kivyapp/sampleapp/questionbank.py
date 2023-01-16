#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random

QUESTIONS = [ 
    {
        "category": "geography",
        "keywords": ["state_capitals", "USA"],
        "level": 1,
        "question": "What is the capital of California?",
        "answerKeys": ["Sacremento", "Fresno", "Los Angeles", "San Francisco"],
        "answer": "Sacremento"
    },
    {
        "category": "geography",
        "keywords": ["state_capitals", "USA"],
        "level": 1,
        "question": "What is the capital of Florida?",
        "answerKeys": ["Orlando", "Miami", "Tallahase", "Jacksolville"],
        "answer": "Tallahase"
    },
    {
        "category": "geography",
        "keywords": ["state_capitals", "USA"],
        "level": 1,
        "question": "What is the capital of Alabama?",
        "answerKeys": ["Jackson", "Fresno", "Los Angeles", "San Francisco"],
        "answer": "Jackson"
    }
]


class QuestionBank():
    def __init__(self):
        self.questionBank = QUESTIONS
        self.questionSet = []
        self.answeredQuestions = []
        self.skippedQuestions = []
        self.wrongAnswers = []
        self.correctAnswers = []


    def createQuestionSet(self, category=None, keyword=None):
        self.questionSet = self.questionBank
        random.shuffle(self.questionSet)

        return self.questionSet

