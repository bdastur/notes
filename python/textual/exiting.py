#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class QuestionApp(App):
    CSS_PATH = "exiting.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Do you love textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


def main():
    app = QuestionApp()
    ret = app.run()
    print("Returned: ", ret)


if __name__ == '__main__':
    main()
