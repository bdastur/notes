#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Using title and subtitle in the app
"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label

class MyApp(App[str]):
    CSS_PATH="titlesubtitle.tcss"
    TITLE = "A Simple Title"
    SUB_TITLE = "A Subtitle"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yesButton", variant="primary")
        yield Button("No", id="noButton", variant="error")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


def main():
    app = MyApp()
    ret = app.run()
    print("Result: ", ret)

if __name__ == '__main__':
    main()