#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Static


class CombiningLayoutApp(App):
    CSS_PATH = "layout01.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range (5):
                    yield Static("Vertical layout. Child %d" % number)
            with Horizontal(id="top-right"):
                yield Static("Horizontally")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("here")
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("Panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout", id="bottom-right-final")


def main():
    app = CombiningLayoutApp()
    app.run()


if __name__ == '__main__':
    main()
