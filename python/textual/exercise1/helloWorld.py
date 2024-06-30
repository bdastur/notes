#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. A simple Textual App.
2. Shows how to add log messages.

"""

from textual.app import App, ComposeResult
from textual.widgets import Welcome
from textual import log


class HelloWorld(App):
    def compose(self) -> ComposeResult:
        print("A simple print. -> prints in devtools console")
        log("Compose hello world. Log message -> logs in devtool console")
        yield Welcome("Hello World, Textual")
    
    def on_button_pressed(self):
        log("Button pressed")

def main():
    app = HelloWorld()

    # NOTE: To run the app in inline mode, you can set the 'inline' parameter
    # to True. Default is False
    app.run(inline=False)


if __name__ == '__main__':
    main()
