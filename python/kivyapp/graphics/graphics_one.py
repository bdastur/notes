#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import kivy.graphics as graphics


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            graphics.Color(1., 1, 0)

            # Add a rectangle
            graphics.Rectangle(pos=kwargs['pos'], size=kwargs['size'])


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        widgetOne = MyWidget(pos=(10, 10), size=(200, 200))
        self.add_widget(widgetOne)

        widgetTwo = MyWidget(pos=(260, 260), size=(200, 200))
        self.add_widget(widgetTwo)



class MainApp(App):
    def build(self):
        return MyLayout()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()
