#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder

from time import strftime

KV = """
<Label>:
    font_name: "Roboto"
    font_size: 90
    markup: True

<RobotButton@Button>:
    font_name: "Roboto"
    font_size: 42

BoxLayout:
    orientation: "vertical"

    Label:
        id: _timeLabel
        text: "[b]00[/b]:00:00"
    
    BoxLayout:
        orientation: "horizontal"
        spacing: 20
        size_hint: (0.4, 0.2)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        RobotButton:
            id: _startStopButton
            text: "Start"
            color: kivy.utils.get_color_from_hex("#e6ecf7")
            background_color: kivy.utils.get_color_from_hex("#961703")
            on_press: app.startStop()
        RobotButton:
            id: _resetButton
            text: "Reset"
            color: kivy.utils.get_color_from_hex("#e6ecf7")
            background_color: kivy.utils.get_color_from_hex("#961703")
            on_press: app.resetStopwatch()
    Label:
        id: _timerLabel
        text: "[b]00[/b]:00:00"
"""
# Builder.load_string(KV)


class ClockApp(App):
    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        self.swStarted = False
        self.swSeconds = 0

    def build(self):
        return Builder.load_string(KV)
    
    def startStop(self):
        print("btnInstance: ")
        if self.root.ids._startStopButton.text == "Start":
            self.swStarted = True
            self.root.ids._startStopButton.text = "Stop"
        else:
            self.swStarted = False
            self.root.ids._startStopButton.text = "Start"
    
    def resetStopwatch(self):
        self.swStarted = False
        self.swSeconds = 0
        self.root.ids._startStopButton.text = "Start"

    def on_start(self):
        print("on start")
        Clock.schedule_interval(self.updateTime, 1)
    
    def updateTime(self, tick):
        print("update time")
        self.root.ids._timeLabel.text = strftime('[b]%H[/b]:%M:%S')

        if self.swStarted:
            self.swSeconds += tick

        m, s = divmod(self.swSeconds, 60)

        self.root.ids._timerLabel.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                            (int(m), int(s), int(s * 100 % 100)))


def main():
    Window.clearcolor = get_color_from_hex("#101216")

    LabelBase.register(name="Roboto",
        fn_regular="/tmp/kivy/Roboto-Regular.ttf",
        fn_bold="/tmp/kivy/Roboto-Bold.ttf",
        fn_italic="/tmp/kivy/Roboto-Italic.ttf",
        fn_bolditalic="/tmp/kivy/Roboto-BoldItalic.ttf")
    ClockApp().run()


if __name__ == '__main__':
    main()
