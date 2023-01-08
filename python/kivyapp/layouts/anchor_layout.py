#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button



class AnchorLayoutExample(App):
    def build(self):
        layout = AnchorLayout(anchor_x='right', anchor_y='center')

        btn = Button(text="Anchored Button")
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(btn)

        return layout
    
    def on_button_press(self, btnInstance):
        print("Button %s pressed" % btnInstance.text)



def main():
    AnchorLayoutExample().run()

if __name__ == '__main__':
    main()