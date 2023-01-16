#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.toast import toast

from kivy.lang.builder import Builder

KV = """
MDScreen:
    MDTopAppBar:
        title: "BottomSheet Example"
        pos_hint: {"top": 1}
        elevation: 2
    MDRaisedButton:
        text: "Open list bottom sheet"
        on_release: app.showItems()
        pos_hint: {"center_x": 0.5, "center_y": 0.05}
        size_hint: 1, 0.1
"""



class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def showItems(self):
        bsMenu = MDListBottomSheet()
        for n in range(5):
            bsMenu.add_item(
                "Standard Item: %d" %n,
                lambda x, y=n: self.itemCallback("Standard item %d" % n)
            )
        bsMenu.open()
    
    def itemCallback(self, *args):
        print("item callback")
        toast(args[0])


def main():
    MainApp().run()

if __name__ == '__main__':
    main()