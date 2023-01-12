#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_file("./page_layout.kv")


class CustomPageLayout(PageLayout):

    def __init__(self, **kwargs):
        super(CustomPageLayout, self).__init__(**kwargs)
        button3 = ObjectProperty()
        # page 1
        # color = get_color_from_hex("#7feb8d")
        # pg1 = Button(text="Page 1", background_color=color, background_normal="")
        # self.add_widget(pg1)

        # pg2 = Button(text="Page 2", background_color=color)
        # self.add_widget(pg2)

        # pg3 = Button(text="Page 3")
        # self.add_widget(pg3)
        # self.page = 2
        print("Main ids: ", self.ids , self.ids['"mycustomButton"'].text)
        self.ids['"mycustomButton"'].text = "This is a text set by parent using id"
        for child in self.children:
            print("Child: ", dir(child))
            print("type of child ", type(child))
            if type(child) == kivy.uix.button.Button:
                print("This is a button ", child.text)

            if isinstance(child, kivy.uix.button.Button):
                print("THis is an instance of a button: ", child.text)
        self.button3.text = "Object property change"




class PageLayoutExample(App):
    def build(self):
        return CustomPageLayout()


def main():
    PageLayoutExample().run()

if __name__ == '__main__':
    main()
