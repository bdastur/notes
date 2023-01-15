#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_file("./mdThree.kv")

class Myscreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(Myscreen, self).__init__(*args, **kwargs)

class MainApp(MDApp):
    def build(self):
        
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        scrn = Myscreen()
        return scrn



def main():
    MainApp().run()

if __name__ == '__main__':
    main()