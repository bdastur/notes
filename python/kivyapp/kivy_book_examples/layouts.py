#!/usr/bin/env python
# -*- coding: utf-8 -*-



from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

Builder.load_file("./layouts.kv")

class MyLayouts(GridLayout):
    pass

class LayoutApp(App):
    def build(self):
        return MyLayouts()


def main():
    LayoutApp().run()

if __name__ == '__main__':
    main()