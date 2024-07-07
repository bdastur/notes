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
from textual.widgets import  Static, Placeholder, Input, Footer, Tab, Tabs
from textual.color import Color
from textual.message import Message


class TabMenu(Tabs):
    DEFAULT_CSS = """
    TabMenu {
        dock: top;
    }
    """
    def __init__(self, menuItems=None, options=None):
        self.tabMenu = None
        self.menuItems = menuItems
        self.tabItems = []
        self.options = options
        self._setMenuTabItems()

        super().__init__()

    def _setMenuTabItems(self):
        # If no menu items are passed, set default/dummy items
        if self.menuItems is None:
            self.tabItems.append(Tab("DummyOne", id="dummy-1"))
            self.tabItems.append(Tab("DummyTwo", id="dummy-2"))
            return

        for item in self.menuItems:
            self.tabItems.append(Tab(item["label"], id=item["id"]))

    def _getMenuItemSelectedCallback(self):
        if self.options is not None:
            if self.options.get("callback", None) is not None:
                return self.options["callback"]

        return None
    
    def getTab(self, tabId):
        for tab in self.tabItems:
            if tab.id == tabId:
                return tab
        return None

    def compose(self) -> ComposeResult:
        self.tabMenu = Tabs(*self.tabItems)
        yield self.tabMenu

    def on_tabs_tab_activated(self, event) -> None:
        print("Tabs class: ", event)
        # for tab in self.tabItems:
        #     if tab.id == event.tab.id:
        #         tab.focus()

        #self.focus(True)
        
        callback = self._getMenuItemSelectedCallback()
        callback(event)


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
    def selectionCallback(self, event):
        print("BRD: Dashboardscreen callback. ", event)
        activeTab = self.tabMenu.getTab("dashboard")
        self.tabMenu._activate_tab(activeTab)

    def setupMenu(self):
        menuItems = [
            {"label": "Dashboard", "id": "dashboard"},
            {"label": "Settings", "id": "settings"},
            {"label": "Profile", "id": "profile"}
        ]
        options = {
            "callback": self.selectionCallback,
            "active": "dashboard"
        }
        self.tabMenu = TabMenu(menuItems=menuItems, options=options)

    def compose(self) -> ComposeResult:
        self.setupMenu()
        yield self.tabMenu
        yield SideMenuBar(id="sideMenubar")
        yield ContentArea(id="contentArea")
        yield Footer()
    
    def on_mount(self):
        activeTab = self.tabMenu.getTab("dashboard")
        self.tabMenu._activate_tab(activeTab)

###############################################################
# Profile Screen components
###############################################################
class ProfileContentArea(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Search Bar", id="searchBar")
        yield Static("Profile Content", id="content")
        
class ProfileScreen(Screen):
    def selectionCallback(self, event):
        print("BRD: Dashboardscreen callback. ", event)
        activeTab = self.tabMenu.getTab("profile")
        self.tabMenu._activate_tab(activeTab)

    def setupMenu(self):
        menuItems = [
            {"label": "Dashboard", "id": "dashboard"},
            {"label": "Settings", "id": "settings"},
            {"label": "Profile", "id": "profile"}
        ]
        options = {
            "callback": self.selectionCallback,
            "active": "profile"
        }
        self.tabMenu = TabMenu(menuItems=menuItems, options=options)

    def compose(self) -> ComposeResult:
        self.setupMenu()
        yield self.tabMenu
        yield SideMenuBar(id="sideMenubar")
        yield ProfileContentArea(id="profileContentArea")
        yield Footer()
    
    def on_mount(self):
        activeTab = self.tabMenu.getTab("profile")
        self.tabMenu._activate_tab(activeTab)



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
    
    def on_tabs_tab_activated(self, event) -> None:
        print("IN Main APP... BRD> HERE ", event)
        if event.tab.id == "profile":
            self.switch_mode("profile")
        elif event.tab.id == "dashboard":
            self.switch_mode("dashboard")


def main():
    app = MainApp()
    ret = app.run()


if __name__ == '__main__':
    main()