#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

from kivy.lang.builder import Builder
Builder.load_file("./toggle_one.kv")


class ToggleOne(App):
    def build(self):
        return ToggleButton()


def main():
    ToggleOne().run()
    

if __name__ == '__main__':
    main()