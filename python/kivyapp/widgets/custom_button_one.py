#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout

class CustomButton():
    def __init__(self):
        self.btn = Button(text="Test Custom Button", 
                          background_color=[0.3, 0.5, 0.9, 1], background_normal="")
        self.btn.color = [0.5, 0.4, 0.6, 1]
        self.btn.backgroud_color = [0.6, 0.4, 0.6, 1]
        self.btn.backgroud_normals = ""


class NavWidget(StackLayout):
    def __init__(self, **kwargs):
        super(NavWidget, self).__init__(**kwargs)
        self.size_hint = [1, 0.2]
        self.padding = [10, 10, 10, 10]
        self.spacing = [5, 0]

        # nav buttons
        homeBtn = Button(text="Home")
        homeBtn.size_hint = [0.2, 1]
        self.add_widget(homeBtn)

        actionBtn = Button(text="Actions")
        actionBtn.size_hint = [0.2, 1]
        self.add_widget(actionBtn)

class LeftMainNavWidget(StackLayout):
    def __init__(self, **kwargs):
        super(LeftMainNavWidget, self).__init__(**kwargs)
        self.size_hint = [0.4, 1]
        self.orientation = "tb-lr"

        # temporary buttons
        btn = Button(text="button 1")
        btn.size_hint = [1, 0.1]
        self.add_widget(btn)
        

        btn2 = Button(text="Button 2")
        btn2.size_hint = [1, 0.1]
        self.add_widget(btn2)
        

class MainAreaWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MainAreaWidget, self).__init__(**kwargs)
        self.cols = 2

        # Left Nav widget
        leftNavWidget = LeftMainNavWidget()
        self.add_widget(leftNavWidget)

        # # Add temporary buttons
        # btn = Button(text="Testing side bar")
        # btn.size_hint = [0.4, 1]
        # self.add_widget(btn)

        btn2 = Button(text="Testing main area")
        self.add_widget(btn2)



class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = "vertical"

        # Add navigation pane at the top.
        navBar = NavWidget()
        self.add_widget(navBar)
        
        # Add Grid Layout
        mainGrid = MainAreaWidget()
        self.add_widget(mainGrid)

        # Add button as a test
        for idx in range(1):
            btn = Button(text="test button %d" % idx)
            btn.size_hint = [1, 0.2]
            self.add_widget(btn)



class RootWidgetOld(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        btnList = []
        btn = Button(text="Simple Button")
        btn.bind(on_press=self.onPressHandler)
        btn.bind(on_touch_down=self.onTouchDown)
        btnList.append(btn)

        btn2 = CustomButton()
        btn2.btn.bind(on_press=self.onPressHandler)
        btnList.append(btn2.btn)

        for btnObj in btnList:
            self.add_widget(btnObj)

    
    
    def onTouchDown(self, instance, pos):
        print("On touch down: ")

    def onPressHandler(self, instance):
        print("onPressHandler, %s" % instance.text)


class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
