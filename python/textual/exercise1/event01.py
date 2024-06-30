#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple example of most basic events.
Here we use the key event. To handle a key press implement the on_key() method.


"""

from typing import Coroutine
from textual.app import App
from textual import events


class EventApp(App):
    COLORS = [
        "white", "red", "green", "yellow", "teal"
    ]

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key)]
    
        
    

def main():
    app = EventApp()
    app.run(inline=False)

if __name__ == '__main__':
    main()
