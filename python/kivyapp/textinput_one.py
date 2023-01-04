#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.lang.builder import Builder

try:
    Builder.load_file("./textinput_one.kv")
except FileNotFoundError:
    print("KV File not found")

class TextInputOne(App):
    def build(self):
        return TextInput()


def main():
    TextInputOne().run()

if __name__ == '__main__':
    main()