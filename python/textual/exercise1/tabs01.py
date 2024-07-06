#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.widgets import Static, Tabs, Tab

NAMES = [
    "Dashboard",
    "Settings",
    "Configuration",
    "Scenarios"
]


class MainApp(App[str]):
    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    Static {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        mytabs = []
        mytabs.append(Tab(NAMES[0], id="dash"))
        mytabs.append(Tab(NAMES[1], id="setting"))
        mytabs.append(Tab(NAMES[2], id="config"))
        mytabs.append(Tab(NAMES[3], id="scenario"))
        myTabs = Tabs(*mytabs)

        self.staticText = Static("This is a test")

        yield myTabs
        yield self.staticText

    def on_mount(self) -> None:
        print("BRD: on mount.")
        self.query_one(Tabs).focus()

    def on_tabs_tab_activated(self, event) -> None:
        print("Tab activate: ", event)
        print("Name: ", event.tab.id, event.tab.label)
        self.staticText.update(event.tab.label)


def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()

