#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.uix.button import MDRectangleFlatIconButton 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex as C


KV = """
#:import C kivy.utils.get_color_from_hex

<MenuButton>:
    #size_hint: [1, 1]
    size_hint_x: 1
    size_y: 50
    icon_color: "orange"
    md_bg_color: C("#432343")

<MyBox>:

#<SideNavLayout>:
#    orientation: "vertical"

"""
#Builder.load_string(KV)

class MenuButton(MDRectangleFlatIconButton):
    pass


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
        buttonOne = ObjectProperty()
        self.buttonOne.bind(on_press=self.buttonClickHandler)

    def buttonClickHandler(self, btnInstance):
        print("Button %s clicked: ", btnInstance.text)


class SideNavLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(SideNavLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.pos_hint = {"center_x": 0.5, "top": 1.0}

        self.navItems = []

    def addNavItem(self, **navItemOption):
        text = navItemOption["text"]
        icon = navItemOption["icon"]

        navItem = MDRectangleFlatIconButton(text=text, icon=icon)
        navItem.size_hint_x = 1
        navItem.size_y = 60
        navItem.md_bg_color = C("#434323")
        navItem.icon_color = C("#FF5667")
        navItem.pos_hint = {"left": 1, "top": 1}

        self.add_widget(navItem)
        self.navItems.append(navItem)
        



