#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.lang.builder import Builder
Builder.load_file("./custom_widget.kv")


class CustomWidget(Widget):
    pass

class TestApp(App):
    def build(self):
        return CustomWidget()


def main():
    TestApp().run()

if __name__ == '__main__':
    main()