#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties  import ObjectProperty

Builder.load_file("./anchor_layout.kv")


class AnchorLayoutExample(AnchorLayout):
    def __init__(self, **kwargs):
        super(AnchorLayoutExample, self).__init__(**kwargs)
        testBbutton = ObjectProperty()
        print("Text: ", self.testButton.text)
        print("Size: ", self.testButton.size)
    


class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayoutExample()
        return layout

        # layout = AnchorLayout(anchor_x='right', anchor_y='center')

        # btn = Button(text="Anchored Button")
        # btn.bind(on_press=self.on_button_press)
        # layout.add_widget(btn)

        # return layout
    
    def on_button_press(self, btnInstance):
        print("Button %s pressed" % btnInstance.text)



def main():
    AnchorLayoutApp().run()

if __name__ == '__main__':
    main()