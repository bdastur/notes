#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.widgets import Welcome

class WelcomeApp(App):
    def compose(self) -> ComposeResult:
        yield Welcome("Hello")

    def on_button_pressed(self) -> None:
        self.exit()


def main():
    app = WelcomeApp()
    app.run()


if __name__ == '__main__':
    main()
