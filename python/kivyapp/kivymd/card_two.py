#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from kivy.properties import StringProperty, ObjectProperty
from kivy.lang.builder import Builder

KV = """

<MyScreen>:
    box: _box

    MDBoxLayout:
        id: _box
        adaptive_size: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "40dp"

<MD3Card>
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"
    
    MDRelativeLayout:
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}
        
        MDLabel:
            id: label
            text: root.text
            pos: "12dp", "10dp"
            adaptive_size: True
            color: "gray"

    """
Builder.load_string(KV)


class MD3Card(MDCard):
    text = StringProperty()


class MyScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)

        box = ObjectProperty()

        styles = {
            "elevated": "#f6eeee",
            "filled": "#f4dedc",
            "outlined": "#f8f5f4"
        }

        for cardStyle in styles.keys():
            card = MD3Card(
                line_color="green",
                style=cardStyle,
                text=cardStyle.capitalize(),
                md_bg_color=styles[cardStyle]
            )
            self.box.add_widget(card)



class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return MyScreen()

def main():
    MainApp().run()


if __name__ == '__main__':
    main()