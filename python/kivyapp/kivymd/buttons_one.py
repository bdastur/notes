#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.lang.builder import Builder

Builder.load_string(
    """
<MyLayout>:
    orientation: "vertical"
    adaptive_height: True
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    spacing: "10dp"

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDFloatingActionButton:
        icon: "language-python"
        md_bg_color: "orange"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDFlatButton:
        text: "MDFlatButton"
        theme_text_color: "Custom"
        text_color: "white"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRaisedButton:
        text: "MDRaisedButton"
        md_bg_color: "red"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRectangleFlatButton:
        text: "MDRectangleFlatButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        icon: "android"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton-No Line"
        icon: "language-python"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: (0, 0, 0, 0)
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRoundFlatIconButton:
        text: "MDRoundFlatIconButton"
        icon: "language-python"
        text_color: "white"
        line_color: "orange"
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
        hint_animation: True
        
      

    """
)

class MyLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

class MainApp(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
    def build(self):  
        self.theme_cls.theme_style = "Dark"
        return MyLayout()

def main():
    MainApp().run()

if __name__ == '__main__':
    main()