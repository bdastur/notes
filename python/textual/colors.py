#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App
from textual import events

class Events(App):
    COLORS = [
        "red",
        "green",
        "white",
        "blue",
        "navy",
        "teal",
        "aqua"
    ]

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            try:
                self.screen.styles.background = self.COLORS[int(event.key)]
            except IndexError: 
                self.screen.styles.background = "darkblue"


def main():
    app = Events()
    app.run()

if __name__ == '__main__':
    main()
