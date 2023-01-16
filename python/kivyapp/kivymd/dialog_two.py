#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

KV = """
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "City"
    MDTextField:
        hint_text: "Street"

MDFloatLayout:
    MDFlatButton:
        text: "Alert Dialog"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.showConfirmationDialog() 
"""

class Content(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        self.dialog = None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def showConfirmationDialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color)
                ]
            )
        self.dialog.open()


def main():
    MainApp().run()

if __name__ == '__main__':
    main()