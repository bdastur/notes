#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In this app, we move the presentation part to the kv file.
In this example, we will load the kv file using the Builder class.
"""

from kivy.app import App
from kivy.uix.label import Label

# Import Build class from kivy.lang
from kivy.lang import Builder

# Exmplictly load the kv file we need
Builder.load_file("./test.kv")

class ThirdApp(App):
    def build(self):
        return Label()


def main():
    ThirdApp().run()

if __name__ == '__main__':
    main()
