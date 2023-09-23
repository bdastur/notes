#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label

class QuestionApp(App):
    # Another way to specify CSS directly within python code, you can
    # set the CSS class variable.
    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
        grid-gutter: 2;
        padding: 2;
    }
    #question {
        width: 100%;
        height: 100%;
        column-span: 2;
        content-align: center bottom;
        text-style: bold;
    }

    Button {
        width: 100%;
    }
    """
    TITLE = "A question App"
    SUB_TITLE = "The most important question"

    def compose(self) -> ComposeResult:
        yield Header()
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
