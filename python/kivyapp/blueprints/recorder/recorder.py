#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang.builder import Builder

KV = """
#:import C kivy.utils.get_color_from_hex

<Button>:
    background_normal: "./button_normal1.png"
    background_down: "./button_down.png"
    background_color: C("#95A5A6")
    halign: "center"
    markup: True
<GridLayout>:
    padding: 10
    spacing: 10
    cols: 2

GridLayout:
    # padding: 15
    # spacing: 10
    # cols: 2
  
    Button:
        background_color: C("#3498DB")
        text: "[font=ModernPictograms][size=120]e[/size][/font] \\nNewRecording"

    GridLayout:
        padding: 0
        # spacing: 10
        # cols: 2
        orientation: "lr-tb"
        Button:
            background_color: C("#1ABC9C")
            text: "bbb1"
        Button:
            background_color: C("#2ECC71")
            text: "bbb2"
        Button:
            background_color: C("#16A085")
            text: "bbb3"
        Button:
            background_color: C("#4EF8FF")
            text: "bbb4"
    Button:
        background_color: C("#E74C3C")
        text: "[font=ModernPictograms][size=80]P[/size][/font] \\nPlayback"
    Button:
        background_color: C("#95A5A6")
        text: "ddd"
    
"""



class MainApp(App):
    def build(self):
        return Builder.load_string(KV)



def main():
    LabelBase.register(name="ModernPictograms", fn_regular="./modernpics.ttf")
    MainApp().run()


if __name__ == '__main__':
    main()