#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex as C
import sys

KV = """
#:import C kivy.utils.get_color_from_hex

<NavItemOne@MDFlatButton>:
    md_bg_color: C("#676767")
    md_icon_color: C("#676869")
    text_color: C("#FF55FF")
    height: 60
    size_hint_x: 1
    pos_hint: {"center_x": 0.5, "top": 1.0}

<NavItemTwo@MDRectangleFlatIconButton>:
    theme_text_color: "Custom"
    text_color: "black"
    line_color: "red"
    height: 60
    size_hint_x: 1
    theme_icon_color: "Custom"
    md_icon_color: C("#676869")
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

<SideNavLayoutOne>:
    orientation: "vertical"
    spacing: 5

    NavItemOne:
        text: "Dashboard"
    NavItemOne:
        text: "Account Settings"
    NavItemOne:
        text: "Reports"
    NavItemOne:
        text: "Tools"

    
    

<SideNavLayoutTwo>:
    orientation: "vertical"
    spacing: 5

    NavItemTwo:
        text: "Dashboard"
        icon: "home"
    NavItemTwo:
        text: "Account Settings"
        icon: "account-settings"

"""
Builder.load_string(KV)


class SideNavLayoutOne(BoxLayout):
    pass

class SideNavLayoutTwo(BoxLayout):
    pass



class MainApp(MDApp):
    def build(self):
        args = sys.argv
        print("args: ", args)
        if len(args) <= 1:
            print("Require a id [1, 2...]")
            sys.exit(1)

        self.theme_cls.primary_palette = "Orange"

        if args[1] == "1":
            return SideNavLayoutOne()
        elif args[1] == "2":
            print("We are here 2")
            return SideNavLayoutTwo()
        
        
        return SideNavLayoutOne()

        

def main():
    MainApp().run()

if __name__ == '__main__':
    main()

