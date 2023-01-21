#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex as C
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

import string

KV = """
#:import C kivy.utils.get_color_from_hex

<IconButton@Button>
    markup: True
    halign: "center"
    background_color: C("#0f0369")
    background_normal: ""
    color: C("#ffffff") 

<DisplayIcons>:
    cols: 18
    orientation: "lr-tb"
    
    
# GridLayout:
#     cols: 6
#     orientation: "lr-tb"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]%a[/size][/font] \\n%a"  
#     IconButton:
#         text: "[font=ModernPictograms][size=120]A[/size][/font] \\nA"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]b[/size][/font] \\nb"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]B[/size][/font] \\nB"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"
#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"

#     IconButton:
#         text: "[font=ModernPictograms][size=120]e[/size][/font] \\ne"
    # CustomButton:
    #     text: "Custom Button"
    #     icon: "e"

"""
Builder.load_string(KV)


class DisplayIcons(GridLayout):
    def __init__(self, **kwargs):
        super(DisplayIcons, self).__init__(**kwargs)
        
        #alphabets = string.ascii_lowercase + string.ascii_uppercase + string.digits
        alphabets = string.printable

        for letter in alphabets:    
            print("Letter: ", letter)
            text = "[font=ModernPictograms][size=120]%c[/size][/font] \n%c"  % (letter, letter)
            btn = Button(text=text, markup=True, halign="center", background_color=C("#0f0369"), 
                         background_normal="", color=("#ffffff"))
            self.add_widget(btn)


class CustomButton(Button):
    icon = ObjectProperty()

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text = "This is a custom Button"
        print("icon: ", self.icon)

class MainApp(App):
    def build(self):
        return DisplayIcons()


def main():
    LabelBase.register(name="ModernPictograms", fn_regular="../resources/modernpics.ttf")
    MainApp().run()


if __name__ == '__main__':
    main()