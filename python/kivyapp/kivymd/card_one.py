#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from kivy.lang.builder import Builder

KV = """
MDScreen:
    MDBoxLayout:
        id: _box
        adaptive_size: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "40dp"

        MDCard:
            id: _mycard
            padding: 4
            size_hint: None, None
            size: "200dp", "100dp"
            style: "elevated"
            line_color: "green"
            md_bg_color: "#f6eeee"
            shadow_softness: 2
            shadow_offset: (0, 1)
            MDRelativeLayout:

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {"top": 1, "right": 1}

                MDLabel:
                    id: _label
                    text: "Elevated"
                    adaptive_size: True
                    color: "grey"
                    pos: "12dp", "12dp"
        
        MDCard:
            id: _mycard
            padding: 4
            size_hint: None, None
            size: "200dp", "100dp"
            style: "filled"
            line_color: "green"
            md_bg_color: "#f4dedc"
            shadow_softness: 12
            shadow_offset: (0, 2)
            MDRelativeLayout:

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {"top": 1, "right": 1}

                MDLabel:
                    id: _label
                    text: "Filled"
                    adaptive_size: True
                    color: "grey"
                    pos: "12dp", "12dp"
        
        MDCard:
            id: _mycard
            padding: 4
            size_hint: None, None
            size: "200dp", "100dp"
            style: "outlined"
            line_color: "green"
            md_bg_color: "#f8f5f4"
            shadow_softness: 12
            shadow_offset: (0, 2)
            MDRelativeLayout:

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {"top": 1, "right": 1}

                MDLabel:
                    id: _label
                    text: "Outlined"
                    adaptive_size: True
                    color: "grey"
                    pos: "12dp", "12dp"
                    bold: True

    """


class MyCard(MDCard):
    def __init__(self, *args, **kwargs):
        super(MyCard, self).__init__(*args, **kwargs)
        


class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

def main():
    MainApp().run()


if __name__ == '__main__':
    main()