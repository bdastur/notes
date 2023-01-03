#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)



class MyMain(App):
    def build(self):
        return LoginScreen()


def main():
    MyMain().run()


if __name__ == '__main__':
    main()
