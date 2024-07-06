#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The example has the following:
1. Grid layout
2. Custom widget that extends Static Widget.
2. Custom message
"""


import sys
import itertools
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.color import Color
from textual.message import Message

class Box(Static):
    GREETINGS = itertools.cycle(
        ["Hello", "Ola", "Salve", "Konnichiwa", "Namaste"]
    )
    class Selected(Message):
        def __init__(self, text: str) -> None:
            self.text = text
            super().__init__()

    def __init__(self, text="Box"):
        self.text = text
        super().__init__()

    def on_mount(self) -> None:
        greeting = next(Box.GREETINGS)
        self.update(greeting)

    def on_click(self) -> None:
        print("Box clicked")
        greeting = next(Box.GREETINGS)
        self.text = greeting
        self.update(greeting)
        self.post_message(self.Selected(self.text))



class GridLayout(App[str]):
    CSS_PATH = "layout01.tcss"

    def compose(self) -> ComposeResult:
        box1 = Box("MyTest Box")
        yield box1
        yield Box("This is a test box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Box("Test Box")
        yield Static("Final Static Box", classes="box")


    def on_click(self, event) -> None:
        print("On click: ", event)

    def on_box_selected(self, msg: Box.Selected) -> None:
        print("Parent: Box selected", msg.text)



def main():
    option = 1
    app = None
    if len(sys.argv) > 1:
        option = sys.argv[1]

    if option == 1:
        app = GridLayout()
    if app is not None:
        ret = app.run()


if __name__ == '__main__':
    main()
