#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label

from kivy.lang.builder import Builder
Builder.load_file("./label_one.kv")

class LableOne(App):
    def build(self):
        return Label()


def main():
    LableOne().run()

if __name__ == '__main__':
    main()