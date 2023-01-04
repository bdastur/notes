#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.carousel import Carousel

from kivy.lang.builder import Builder
Builder.load_file("carousel_one.kv")


class CarouselApp(App):
    def build(self):
        return Carousel()


def main():
    CarouselApp().run()

if __name__ == '__main__':
    main()
