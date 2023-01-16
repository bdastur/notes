#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy_garden.graph import Graph


from kivy.lang.builder import Builder

KV = """
MDFloatLayout:
    MDFlatButton:
        text: "Alert Dialog"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.show_alert_dialog()
"""

class MainApp(MDApp):
    def build(self):
        self.dialog = None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text = "Discard Draft?",
                buttons = [
                    MDFlatButton(
                        text="cancel",
                        theme_text_color = "Custom",
                        text_color = self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="close",
                        theme_text_color = "Custom",
                        text_color = self.theme_cls.primary_color,
                        on_press=self.dismissDialog
                    )
                ]
            )
        self.dialog.open()
    
    def dismissDialog(self, dialogItem):
        self.dialog.dismiss()



def main():
    MainApp().run()


if __name__ == '__main__':
    main()