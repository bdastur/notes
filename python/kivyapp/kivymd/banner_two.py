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
       


class MainApp(MDApp):
    title = "Banner test"

    def build(self):
        print("MainApp start")
        return ExampleBanner()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()