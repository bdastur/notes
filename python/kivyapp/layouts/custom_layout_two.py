#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An example using screen manager
"""

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
from kivy.properties import ObjectProperty

from kivy.lang.builder import Builder

Builder.load_file("./custom_layout_two.kv")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

     

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm


def main():
    MainApp().run()

if __name__ == '__main__':
    main()
