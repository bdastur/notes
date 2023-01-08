#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.label import Label

from kivy.lang.builder import Builder
Builder.load_file("./hello.kv")


class HelloApp(App):
    def build(self):
        return Label()


def main():
    HelloApp().run()


if __name__ == '__main__':
    main()