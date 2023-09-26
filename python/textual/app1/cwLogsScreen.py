#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder, Header, Footer



class CWLogsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Placeholder("A temporary placeholder")
        yield Placeholder("A temporary placeholder")
