#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
Builder.load_file("./widgetsOne.kv")


class MyWidget(Widget):
    pass


class WidgetsApp(App):
    def build(self):
        return MyWidget()


def main():
    WidgetsApp().run()

if __name__ == '__main__':
    main()