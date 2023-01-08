#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder

Builder.load_file("./page_layout.kv")


class CustomPageLayout(PageLayout):
    def __init__(self, **kwargs):
        super(CustomPageLayout, self).__init__(**kwargs)

        # page 1
        color = get_color_from_hex("#7feb8d")
        pg1 = Button(text="Page 1", background_color=color, background_normal="")
        self.add_widget(pg1)

        pg2 = Button(text="Page 2", background_color=color)
        self.add_widget(pg2)

        pg3 = Button(text="Page 3")
        self.add_widget(pg3)

        self.page = 2
        


class PageLayoutExample(App):
    def build(self):
        return CustomPageLayout()


def main():
    PageLayoutExample().run()

if __name__ == '__main__':
    main()