#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder, Header, Footer
import mainScreen 
import cwLogsScreen

       

class MainApp(App):
    CSS_PATH = "cwlogs.tcss"
    # SCREENS = {"main": mainScreen.MainScreen(id="main-screen"),
    #            "cwlogs": cwLogsScreen.CWLogsScreen(id="cwlogsScreen") } 
    # BINDINGS=[("m", "switch_screen('main')", "MainScreen"),
    #            ("c", "switch_screen('cwlogs')", "CWLogsScreen")]
    
    def on_mount(self) -> None:
        self.title = "Cloud Tools"
        self.push_screen(cwLogsScreen.CWLogsScreen(id="cwlogsScreen"))
        # self.push_screen(mainScreen.MainScreen(id="main-screen"))
        # self.switch_screen(cwLogsScreen.CWLogsScreen(id="cwlogsScreen"))


def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()
