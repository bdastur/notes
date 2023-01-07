#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.lang.builder import Builder
Builder.load_file("./float_layout.kv")


class TestApp(App):
    def build(self):
        return FloatLayout()


def main():
    TestApp(title="Float Layout").run()

if __name__ == '__main__':
    main()