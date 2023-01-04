#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.button import Button

from kivy.lang.builder import Builder
Builder.load_file("./button_one.kv")


class ButtonApp(App):
    def build(self):
        return Button()


def main():
    ButtonApp().run()
    

if __name__ == '__main__':
    main()