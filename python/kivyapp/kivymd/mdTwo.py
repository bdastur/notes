#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "800"

        return (
            MDScreen(
                MDRaisedButton(
                    text="Raised Button",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
            )
        )


def main():
    MainApp().run()

if __name__ == '__main__':
    main()