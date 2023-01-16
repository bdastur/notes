#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton

from kivy.lang.builder import Builder

KV = """
GridLayout:
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
            text: "What is the capital of California?"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: "orange"
            size_hint: (1.0, 1.0)
        MDRaisedButton:
            text: "A: Sacremento"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            text: "B: San Jose"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            text: "C: Los Angeles"
            size_hint: (1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
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



    #MDRaisedButton:
    #    text: "Bottom"
    #    size_hint: (1.0, 0.2)
    #    pos_hint: {"center_x": 0.5, "center_y": 0.5}

"""



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


def main():
    MainApp().run()


if __name__ == '__main__':
    main()



