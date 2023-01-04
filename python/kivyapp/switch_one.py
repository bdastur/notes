#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        return Switch()


def main():
    SwitchApp().run()

if __name__ == '__main__':
    main()