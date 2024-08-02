#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, SelectionList


class MainApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    SelectionList {
        padding: 1;
        border: solid $accent;
        width: 40%;
        height: 30%;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header(name="Selection list", show_clock=True)
        yield Label("This is a test")
        yield SelectionList(("Behzad Dastur", 0, True),
                             ("Parinaz Dastur", 1),
                             ("Delnavaz Dastur", 2, True),
                             ("Afreed Mistry", 3, False))
        yield Footer()
    
    def on_selection_list_selection_toggled(self, event) -> None:
        print("On selected change: ", event)


def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()
