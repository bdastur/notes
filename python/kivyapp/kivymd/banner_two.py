#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.banner import MDBanner
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar

from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_file("./banner_two.kv")

class ExampleBanner(MDScreen):
    def __init__(self, *args, **kwargs):
        super(ExampleBanner, self).__init__(*args, **kwargs)
        self.bannerActive = False

        banner = ObjectProperty()
        self.banner.detect_visible = False
        self.banner.bind(on_enter=self.bannerEnter)
        self.banner.bind(on_release=self.bannerRelease)

        listItemOne = ObjectProperty()
        listItemTwo = ObjectProperty()
        listItemThree = ObjectProperty()

        self.listItemOne.bind(on_press=self.itemOnePress)
        self.listItemTwo.bind(on_press=self.itemTwoPress)
        self.listItemThree.bind(on_press=self.itemThreePress)
    
    def bannerEnter(self, bannerItem):
        print("Banner on enter: ", bannerItem.text)

    def bannerRelease(self, bannerItem):
        self.bannerActive = False

    def itemOnePress(self, item):
        self.banner.type = "one-line"
        self.banner.text = ["One line banner"]
        self.banner.left_action = ["cancel", lambda x: None]
        self.banner.right_action = ["close", lambda x: self.banner.hide()]
        if not self.bannerActive:
            self.banner.show()
            self.bannerActive = True
    
    def itemTwoPress(self, item):
        self.banner.type = "one-line-icon"
        self.banner.text = ["One line string text example without actions."]
        self.banner.left_action = []
        self.banner.right_action = []
        if not self.bannerActive:
            self.banner.show()
            self.bannerActive = True

    
    def itemThreePress(self, item):
        self.banner.type = "two-line-icon"
        self.banner.text = [ 
            "One line string text example with two actions.",
            "This is the second line of the banner message."]
        self.banner.left_action = ["CANCEL", lambda x: None]
        self.banner.right_action = ["CLOSE", lambda x: self.banner.hide()]

        if not self.bannerActive:    
            self.banner.show()
            self.bannerActive = True




class MainApp(MDApp):
    title = "Banner test"

    def build(self):
        print("MainApp start")
        return ExampleBanner()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()