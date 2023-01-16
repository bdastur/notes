#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp

from kivy.lang.builder import Builder

KV = """
MDCarousel:
    rows: 2
    MDScreen:
        MDBoxLayout:
            orientation: "vertical"
            pos_hint: {"center_x": 0.5, "center_y": 1}
            spacing: "10dp"
            MDRectangleFlatButton:
                text: "What is the capital of California?"
                theme_text_color: "Custom"
                text_color: "yellow"
                line_color: "red"
                pos_hint: {"center_x": 0.5, "center_y": 0.2}
            MDRaisedButton:
                text: "A: San Francisco"
                md_bg_color: "orange"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDFlatButton:
                text: "B: Sacremento"
                theme_text_color: "Custom"
                text_color: "yellow"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDRaisedButton:
                text: "C: San Diego"
                md_bg_color: "orange"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDScreen:
        Button:
            text: "Button one"
    
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


def main():
    MainApp().run()


if __name__ == '__main__':
    main()