#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import OptionProperty


class BoxLayoutApp(App):
    def build(self):

        layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)
        buttons = []    
        for i in range(5):
            buttonText = "Button %d" % i
            btn = Button(text=buttonText)
            btn.bind(on_press=self.on_button_press_handler)

            buttons.append(btn)
            layout.add_widget(btn)
        return layout
    
    def on_button_press_handler(self, instance):
        print("Button pressed ", instance.text)



def main():
    BoxLayoutApp().run()

if __name__ == '__main__':
    main()