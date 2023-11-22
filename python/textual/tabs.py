#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Tabs


NAMES = [
    "Paul Atreidies",
    "Lady Jessica",
    "Chani",
    "Silgar"
]

class MainApp(App):
    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    Label {
        margin: 1 1;
        width: 100%;
        height: 100%;
        background: $panel;
        border: tall $primary;
        content-align:  center middle;
    }

    """
    def compose(self) -> ComposeResult:
        yield Header(name="Tabs Example")
        yield Tabs(NAMES[0], NAMES[1])
        yield Label()
        yield Footer()
    
    
    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """Handle TabActivated message sent by Tabs."""
        print("Tabs activated ", event.tab)
        label = self.query_one(Label)
        if event.tab is None:
            # When the tabs are cleared, event.tab will be None
            label.visible = False
        else:
            label.visible = True
            label.update(event.tab.label)
       



def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()