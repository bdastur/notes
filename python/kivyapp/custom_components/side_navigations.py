#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.uix.button import MDRectangleFlatIconButton 
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex as C

KV = """
BoxLayout:
    orientation: "vertical"
    Button:
        text: "Testing"
    Button:
        text: "Testing"
"""


class SideNavLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(SideNavLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.background_color = C("#334433")
        self.color = C("#223344")
        self.padding = 0
        self.spacing = 5
        self.navItems = []
        self.itemProperties = {}
        self.setItemProperties()


    def setItemProperties(self, height=60, md_bg_color="#434343", icon_color="#764333", 
                          text_color="#ffffff"):
        self.itemProperties["height"] = height
        self.itemProperties["md_bg_color"] = C(md_bg_color)
        self.itemProperties["icon_color"] = C(icon_color)
        self.itemProperties["text_color"] = C(text_color)


    def addNavItem(self, text, icon=None):

        if icon is not None:
            navItem = MDRectangleFlatIconButton(text=text, icon=icon)
        else:
            navItem = MDRectangleFlatIconButton(text=text)
        navItem.size_hint_x = 1
        navItem.pos_hint = {"left": 1, "top": 1}

        navItem.height = self.itemProperties["height"] = 60
        navItem.md_bg_color = self.itemProperties["md_bg_color"]
        navItem.icon_color = self.itemProperties["icon_color"]
        

        self.add_widget(navItem)
        self.navItems.append(navItem)
        



