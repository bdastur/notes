#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.checkbox import CheckBox

from kivy.lang.builder import Builder
Builder.load_file("./checkbox_one.kv")


class CheckboxOne(App):
    def build(self):
        return CheckBox()



def main():
    CheckboxOne().run()


if __name__ == '__main__':
    main()