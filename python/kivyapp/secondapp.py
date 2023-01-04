#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In this app, we move the presentation part to the kv file.
We will use naming convention here. 
Create a file called second.kv, which is basically based on 
the class name 'SecondApp'. 

"""

from kivy.app import App
from kivy.uix.label import Label


class SecondApp(App):
    def build(self):
        return Label()


def main():
    SecondApp().run()

if __name__ == '__main__':
    main()
