#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivy.lang.builder import Builder

Builder.load_file("./custom_layout_one.kv")


class CustomLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        pageOneButton = ObjectProperty()
        pageTwoButton = ObjectProperty()
        pageThreeButton = ObjectProperty()
        pageFourButton = ObjectProperty()
        layoutPage = ObjectProperty()

        self.pageOneButton.bind(on_press=self.buttonOnePressHandler)
        self.pageTwoButton.bind(on_press=self.buttonTwoPressHandler)
        self.pageThreeButton.bind(on_press=self.buttonThreePressHandler)
        self.pageFourButton.bind(on_press=self.buttonFourPressHandler)
    
    def buttonOnePressHandler(self, instance):
        print("Text: ", instance.text)
        self.layoutPage.page = 0

    def buttonTwoPressHandler(self, instance):
        print("Text: ", instance.text)
        self.layoutPage.page = 1
    
    def buttonThreePressHandler(self, instance):
        print("Text: ", instance.text)
        self.layoutPage.page = 2
    
    def buttonFourPressHandler(self, instance):
        print("Text: ", instance.text)
        self.layoutPage.page = 3




class MainApp(App):
    def build(self):
        return CustomLayout()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()