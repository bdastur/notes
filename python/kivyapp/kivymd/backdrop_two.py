#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior

from kivy.properties import StringProperty, BooleanProperty
from kivy.lang.builder import Builder
Builder.load_file("./backdrop_two.kv")

class MyBackdrop(MDScreen):
    pass

class ItemBackdropBackLayer(ThemableBehavior, MDBoxLayout):
    icon = StringProperty("andrid")
    text = StringProperty()
    selected_item = BooleanProperty(False)
    

class MainApp(MDApp):
    title = "Electronic supplies"
    def build(self):
        return MyBackdrop()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()
