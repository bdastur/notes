#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivymd.app import MDApp

from kivy.lang.builder import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Blue"

        return(Builder.load_string(
            """
MDScreen:
    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        md_bg_color: app.theme_cls.primary_color
        use_text: True

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: 'numeric-10'

            MDLabel:
                text: 'Mail'
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'twitter'
            badge_icon: 'numeric-5'

            MDLabel:
                text: 'Twitter'
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIn'
            icon: 'linkedin'
            badge_icon: 'numeric-2'

            MDLabel:
                text: 'LinkedIn'
                halign: 'center'

            """
        ))


def main():
    MainApp().run()

if __name__ == '__main__':
    main()