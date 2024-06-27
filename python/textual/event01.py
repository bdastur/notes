#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Coroutine
from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input, Button
from textual.strip import Strip
from rich.segment import Segment

#class CustomInput(Input):


class MainApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("ctrl+c", "quit", "Quit")]

    inputText = None
    def compose(self) -> ComposeResult:
        self.inputText = Input("test", id="input01")
        yield self.inputText
        yield Button("Submit", id="button01")

    
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        buttonId = event.button.id
        print("BRD: Button pressent: ", buttonId, self.inputText.value)
      



if __name__ == "__main__":
    app = MainApp()
    app.run()

