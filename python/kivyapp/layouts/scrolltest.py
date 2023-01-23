#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex as C
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

import string

LabelBase.register(name="ModernPictograms", fn_regular="../resources/modernpics.ttf")

layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))

letters = string.printable
#for i in range(100):
for letter in letters:
    text = "[font=ModernPictograms][size=120]%c[/size][/font] \n%c"  % (letter, letter)
    btn = Button(text=text, markup=True, halign="center", background_color=C("#0f0369"),
                 background_normal="", color=("#ffffff"))

    #btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)



runTouchApp(root)
