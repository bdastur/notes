#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex as C

import custom_components.side_navigations as sidenavs

KV = """
#:import C kivy.utils.get_color_from_hex

<MenuButton>:
    size_hint_x: 1
    size_y: 50
    icon_color: "orange"
    md_bg_color: C("#432343")

<MyBox>:
    buttonOne: _buttonOne

    orientation: "vertical"
    spacing: 10
    padding: 10
    MenuButton:
        text: "Test Button"
        icon: "email-open"
    Button:
        id: _buttonOne
        text: "Test Button 1"
        background_color: C("#535533")
    Button:
        id: _buttonTwo
        text: "Test Button 2"
        background_color: C("#535533")
        background_normal: ""
        on_press: root.buttonClickHandler(_buttonTwo)
    Button:
        id: _buttonThree
        text: "Test Button 3"
        background_color: C("#535533")
    MDRaisedButton:
        id: _buttonFour
        text: "MD Test Button 4"
        size_hint: [1, 1]
        md_bg_color: C("#535533")
    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton-No Line"
        size_hint: [1, 1]
        icon: "language-python"
        theme_text_color: "Custom"
        text_color: C("#545455")
        line_color: (0, 0, 0, 0)
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        size_hint: [1, 1]
        icon: "language-python"
        theme_text_color: "Custom"
        #text_color: C("#545455")
        md_bg_color: C("#535533")
        theme_icon_color: "Custom"
        icon_color: "darkgreen"
        #pos_hint: {"center_x": 0.5, "center_y": 0.5}



"""
Builder.load_string(KV)

class MenuButton(MDRectangleFlatIconButton):
    pass


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
        buttonOne = ObjectProperty()
        self.buttonOne.bind(on_press=self.buttonClickHandler)

    def buttonClickHandler(self, btnInstance):
        print("Button %s clicked: ", btnInstance.text)



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"

        #myNav = sidenavs.MyBox()
        myNav = sidenavs.SideNavLayout()

        navItemInfo = {
            "text": "This is a test",
            "icon": "email-open"
        }
        myNav.addNavItem(**navItemInfo)
        navItemInfo = {
            "text": "This is a second button",
            "icon": "email-open"
        }
        #myNav.addNavItem(**navItemInfo)

        return myNav


def main():
    MainApp().run()

if __name__ == '__main__':
    main()

