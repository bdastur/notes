#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The example has the following:
1. Grid layout
2. Custom widget that extends Static Widget.
2. Custom message
"""


import sys
import itertools
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, VerticalScroll, Horizontal
from textual.widgets import Button, Static, Placeholder, Input, Footer, Header
from textual.color import Color
from textual.message import Message


###############################################################
# Main Dashboard Screen components
###############################################################

class SideMenuBar(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Static("This is a test", classes="menuItem")
        yield Placeholder("Menu item one", classes="menuItem")
        yield Placeholder("Menu item two", classes="menuItem")
        yield Placeholder("Menu item three", classes="menuItem")
        yield Placeholder("Menu item four", classes="menuItem")

class ContentArea(Container):
    def compose(self) -> ComposeResult:
        yield Static("Search Bar", id="searchBar")
        yield Static("Content", id="content")

# Dashboard screen
class MainDashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        yield SideMenuBar(id="sideMenubar")
        yield ContentArea(id="contentArea")
        yield Footer()

###############################################################
# Profile Screen components
###############################################################
class ProfileContentArea(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Search Bar", id="searchBar")
        yield Static("Profile Content", id="content")
        
class ProfileScreen(Screen):
    def compose(self) -> ComposeResult:
        yield SideMenuBar(id="sideMenubar")
        yield ProfileContentArea(id="profileContentArea")
        yield Footer()



class MainApp(App[str]):
    CSS_PATH = "screen01.tcss"
    BINDINGS = [
        ("d", "switch_mode('dashboard')", "Dashboard"),
        ("p", "switch_mode('profile')", "Profile")
    ]
    MODES = {
        "dashboard": MainDashboardScreen,
        "profile": ProfileScreen
    }
    
    def on_mount(self) -> None:
        self.switch_mode("dashboard")


def main():
    app = MainApp()
    ret = app.run()


if __name__ == '__main__':
    main()