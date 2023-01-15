#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.backdrop import MDBackdrop

from kivy.lang.builder import Builder
Builder.load_file("./backdrop_one.kv")


class MyBackDrop(MDBackdrop):
    def __init__(self, *args, **kwargs):
        super(MyBackDrop, self).__init__(*args, **kwargs)




class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"

        myBackdrop = MyBackDrop()
        return myBackdrop


def main():
    MainApp().run()

if __name__ == '__main__':
    main()