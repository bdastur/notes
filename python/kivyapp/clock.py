#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout


class MyClock(GridLayout):
    def __init__(self, **kwargs):
        super(MyClock, self).__init__(**kwargs)
        self.cols = 1
        self.myLabel = Label(text="Clock: ")
        self.add_widget(self.myLabel)

        Clock.schedule_once(self.clockCallback, 3)
    
    def clockCallback(self, duration):
        now = datetime.datetime.now()
        print("Duration: ", datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))
        self.myLabel.text = "Clock: %s" % datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")


class ClockApp(App):
    def build(self):
        myclock = MyClock()

        Clock.schedule_interval(myclock.clockCallback, 5)


        return myclock


def main():
    ClockApp().run()

if __name__ == '__main__':
    main()
        