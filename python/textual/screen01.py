#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static

class BSOD(Screen):
    ERROR_TEXT = """
        This is an error screen!.
        Here you can take corrective action.
    """
    def compose(self) -> ComposeResult:
        yield Static("Windows", id="title")
        yield Static(self.ERROR_TEXT)
        yield Static("Press any key to continue", id="any-key")


class ScreenApp(App):
    CSS_PATH="screen01.tcss"
    SCREENS = {"bsod": BSOD()}
    BINDINGS = [("b", "push_screen('bsod')", "BSOD")]


def main():
    app = ScreenApp()
    app.run()

if __name__ == '__main__':
    main()
