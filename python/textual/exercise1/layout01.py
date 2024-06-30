#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.color import Color

class Box(Static):
    GREETINGS = itertools.cycle(
        ["Hello", "Ola", "Salve", "Konnichiwa", "Namaste"]
    )

    def __init__(self, text="Box"):
        self.text = text
        super().__init__()
    
    def on_mount(self) -> None:
        greeting = next(Box.GREETINGS)
        self.update(greeting)

    def on_click(self) -> None:
        print("BOx clicked")
        greeting = next(Box.GREETINGS)
        self.update(greeting)

    


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
        yield Static("One", classes="box")
       
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        buttonId = self.event.button.id
        print("BRD: Buttonid ", buttonId)
        self.exit(buttonId)
    
    def on_click(self, event) -> None:
        print("On click: ", event)

        


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