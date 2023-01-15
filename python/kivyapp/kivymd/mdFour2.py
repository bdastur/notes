#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

import random


Builder.load_file("./mdFour2.kv")


class MyScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(MyScreen, self).__init__(*args, **kwargs)
        palletteButton = ObjectProperty()
        self.palletteButton.bind(on_press=self.switchThemePallettes)
    
    def switchThemePallettes(self, btnInstance):
        print("Switch theme pallettes in Myscreen: ", btnInstance.text)
      

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        mScreen = MyScreen()
        mScreen.palletteButton.bind(on_release=self.switch_theme_pallette)

        return mScreen
    
    # For modifying App level values, like theme sytels and pallette. It makes sense to have
    # the handlers defined here
    def switch_theme_style(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
    
    def switch_theme_pallette(self, btnInstance):
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