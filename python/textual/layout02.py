#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Static, Placeholder, Input, Label, Button



class SideMenuBar(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Placeholder("Menu item one", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")



class InputArea(Container):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Text input", id="input01")
        yield Button("Submit", id="button01")

class ResultAreaVerticalScroll(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield ResultArea(id="resultArea")
        yield ResultAreaTwo(id="resultAreaTwo")


class ResultArea(Container):
    def compose(self) -> ComposeResult:
        yield Placeholder("Result Item one", classes="resultItems")
        yield Placeholder("Result Item two", classes="resultItems")
        yield Placeholder("Result Item three", classes="resultItems")
        yield Placeholder("Result Item four", classes="resultItems")
        yield Placeholder("Result Item five", classes="resultItems")
        yield Placeholder("Result Item six", classes="resultItems")
        yield Placeholder("Result Item seven", classes="resultItems")
        yield Placeholder("Result Item eight", classes="resultItems")
        yield Placeholder("Result Item nine", classes="resultItems")
        # Note that since Result area is a grid, it does not scroll. 
        # we should probably put this within a vertical scroll
        yield Placeholder("Result Item ten", classes="resultItems")
        yield Placeholder("Result Item eleven", classes="resultItems")
        yield Placeholder("Result Item twelve", classes="resultItems")


class ResultAreaTwo(Container):
    def compose(self) -> ComposeResult:
        # Note that since Result area is a grid, it does not scroll. 
        # we should probably put this within a vertical scroll
        yield Placeholder("Result Item ten", classes="resultItems")
        yield Placeholder("Result Item eleven", classes="resultItems")
        yield Placeholder("Result Item twelve", classes="resultItems")
        yield Placeholder("Result Item thrteen", classes="resultItems")
        yield Placeholder("Result Item fourteen", classes="resultItems")
        yield Placeholder("Result Item fifteen", classes="resultItems")


class ContentArea(Container):
    def compose(self) -> ComposeResult:
        yield InputArea(id="inputArea")
        yield ResultAreaVerticalScroll(id="resultAreaVerticalScroll")
        #yield ResultArea(id="resultArea")


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield SideMenuBar(id="sideMenubar")
        yield ContentArea(id="contentArea")


class MainApp(App):
    CSS_PATH = "layout02.tcss"
    def on_mount(self) -> None:
        self.push_screen(MainScreen(id="mainScreen"))


def main():
    mainApp = MainApp()
    mainApp.run()

if __name__ == '__main__':
    main()
