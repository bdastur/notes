#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

import random


#Builder.load_file("./mdFour.kv")


class MyScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(MyScreen, self).__init__(*args, **kwargs)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("./mdFour1.kv")
    
    def switch_theme_style(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
    
    def switch_theme_pallette(self):
        pallette =  ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 
                     'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 
                     'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 
                     'BlueGray']

        print("Setting pallette")
        randNum = random.randint(0, len(pallette)-1)
        self.theme_cls.primary_palette = pallette[randNum]


def main():
    MainApp().run()

if __name__ == '__main__':
    main()