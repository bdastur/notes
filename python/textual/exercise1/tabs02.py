#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Coroutine
from textual.app import App, ComposeResult
from textual.widgets import Static, Tabs, Tab
from textual.screen import Screen


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

    def compose(self) -> ComposeResult:
        self.tabMenu = Tabs(*self.tabItems)
        yield self.tabMenu

    def on_tabs_tab_activated(self, event) -> None:
        print("Tabs class: ", event)
        callback = self._getMenuItemSelectedCallback()
        callback(event)


class DashboardScreen(Screen):
    def selectionCallback(self, event):
        print("BRD: Dashboardscreen callback. ", event)

    def setupMenu(self):
        menuItems = [
            {"label": "Dashboard", "id": "dashboard"},
            {"label": "Settings", "id": "settings"},
            {"label": "Profile", "id": "profile"}
        ]
        options = {
            "callback": self.selectionCallback
        }
        self.tabMenu = TabMenu(menuItems=menuItems, options=options)


    def compose(self) -> ComposeResult:
        self.setupMenu()
        yield self.tabMenu
        yield Static("Dashboard 1")
        yield Static("Dashboard 2")

# Main.
def menuItemSelectionCallback(event):
    print("BRD: Menu item selected. Callback", event)


class MainApp(App[str]):
    CSS = """
    Screen {
        align: center middle;
        border: green;
        margin: 2 2;
        padding-left: 1;
    }
    Static {
        align: center middle;
    }
    """
    def selectionCallback(self, event):
        print("BRD: MainApp callback. ", event)

    def compose(self) -> ComposeResult:
        self.staticText = Static("This is a test")
        menuItems = [
            {"label": "Dashboard", "id": "dashboard"},
            {"label": "Settings", "id": "settings"},
            {"label": "Profile", "id": "profile"}
        ]
        options = {
            "callback": self.selectionCallback
        }
        self.tabMenu = TabMenu(menuItems=menuItems, options=options)

        yield self.tabMenu
        yield self.staticText

    def on_mount(self) -> None:
        print("BRD: on mount.")
        # self.query_one(TabMenu).focus()

    def on_tabs_tab_activated(self, event) -> None:
        print("Tab activate: ", event)
        print("Name: ", event.tab.id, event.tab.label)
        self.staticText.update(event.tab.label)
        if event.tab.id == "settings":
            self.push_screen(DashboardScreen())


def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()

