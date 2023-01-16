#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.clock import Clock

import json
import random
import questionbank


KV = """
<MainAppScreen>:
    question: _question
    answerKey1: _answerKey1
    answerKey2: _answerKey2
    answerKey3: _answerKey3
    answerKey4: _answerKey4

    rows: 3
    orientation: "tb-lr"
    spacing: 5
    MDRaisedButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: (1.0, 0.1)
        text: "Ultimate Trivia"
    BoxLayout:
        orientation: "vertical"
        spacing:  "5dp"
        MDLabel:
            id: _question
            text: "What is the capital of California?"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: "green"
            size_hint: (1.0, 1.0)
        MDRaisedButton:
            id: _answerKey1
            text: "A: Sacremento"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            id: _answerKey2
            text: "B: San Jose"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            id: _answerKey3
            text: "C: Los Angeles"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            id: _answerKey4
            text: "A: Fresno"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDBoxLayout:
        orientation: "horizontal"
        background_color: "lightgrey"
        size_hint: (1.0, 0.1)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "20dp"
        MDIconButton:
            icon: "animation-play"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDIconButton:
            icon: "application-settings"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

"""
Builder.load_string(KV)

class MainAppScreen(GridLayout):
    def __init__(self, *args, **kwargs):
        super(MainAppScreen, self).__init__(*args, **kwargs)
        self.qbObj = questionbank.QuestionBank()

        self.questionSet = self.qbObj.createQuestionSet() 
        self.idx = 0
        self.answerSelected = False

        question = ObjectProperty()
        answerKey1 = ObjectProperty()
        answerKey2 = ObjectProperty()
        answerKey3 = ObjectProperty()
        answerKey4 = ObjectProperty()

        self.answerKeys = [self.answerKey1, self.answerKey2, 
                           self.answerKey3, self.answerKey4]

        self.answerKey1.bind(on_press=self.answerClickHandler)
        self.answerKey2.bind(on_press=self.answerClickHandler)
        self.answerKey3.bind(on_press=self.answerClickHandler)
        self.answerKey4.bind(on_press=self.answerClickHandler)

        import pdb; pdb.set_trace()


    def clockCallback(self, duration):
        self.populateQuestionInfo()

    def populateQuestionInfo(self):
        idx = random.randint(0, len(self.questionSet) - 1)
        self.idx = idx
        self.answerSelected = False

        self.question.text = self.questionSet[idx]['question']
        random.shuffle(self.questionSet[idx]['answerKeys'])

        count = 0
        for answerKey in self.answerKeys:
            answerKey.md_bg_color = "orange"
            answerKey.text = self.questionSet[idx]['answerKeys'][count]
            count += 1


    def answerClickHandler(self, btnInstance):
        if self.answerSelected:
            return

        if self.questionSet[self.idx]['answer'] == btnInstance.text:
            print("You answered correctly")
            btnInstance.md_bg_color = "lightgreen"
        else:
            print("You did not answer correctly")
            btnInstance.md_bg_color = "#e38899"



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        mainApp = MainAppScreen()
        mainApp.populateQuestionInfo()

        Clock.schedule_interval(mainApp.clockCallback, 5)
        return mainApp


def main():
    MainApp().run()


if __name__ == '__main__':
    main()



