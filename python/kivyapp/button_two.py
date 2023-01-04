#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This example shows creating the Button in the python code, instead of the KV file.
"""

from kivy.app import App
from kivy.uix.button import Button

button = Button(text="Button Two!", font_size=40)


def on_press_callback(instance):
    print("on press callback")
    instance.font_size = 100
    instance.text = "Pressed"

def on_release_callback(instance):
    print("on release callback")
    instance.font_size = 60
    instance.text = "Released"

button.bind(on_press=on_press_callback)
button.bind(on_release=on_release_callback)


class ButtonTwo(App):
    def build(self):
        return button


def main():
    button = ButtonTwo()
    button.run()


if __name__ == '__main__':
    main()