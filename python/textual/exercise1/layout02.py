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
from textual.screen import Screen
from textual.containers import Container, VerticalScroll, Horizontal
from textual.widgets import Button, Static, Placeholder, Input
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

###########################################################
# SideMenu bar
###########################################################
class SideMenuBar(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Placeholder("Menu item one", classes="menuItem")
        yield Placeholder("Menu item two", classes="menuItem")
        yield Placeholder("Menu item three", classes="menuItem")
        yield Placeholder("Menu item four", classes="menuItem")


###########################################################
# Content Area Items
###########################################################

class TopInputArea(Container):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search...", id="inputSearch")
        yield Button("Search", id="buttonSearch")

class ContentArea(Container):
    def compose(self) -> ComposeResult:
        yield TopInputArea(id="topInputArea")
        yield Static("Content Area")


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield SideMenuBar(id="sideMenuBar")
        yield ContentArea(id="contentArea")


class MainApp(App[str]):
    CSS_PATH = "layout02.tcss"
    def on_mount(self) -> None:
        self.push_screen(MainScreen(id="mainScreen"))



def main():
    option = 1
    app = None
    if len(sys.argv) > 1:
        option = sys.argv[1]

    if option == 1:
        app = MainApp()
    if app is not None:
        ret = app.run()


if __name__ == '__main__':
    main()
