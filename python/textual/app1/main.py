#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, VerticalScroll
from textual.widgets import Checkbox, Static, Placeholder, Header, Footer
import mainScreen 

# class RegionCheckBox(Checkbox):
#     checked = False 
#     def on_click(self) -> None:
#         print("BRD: here on click: ", self, self.id)
#         self.checked = True

#     def on_region_checkbox_changed(checkbox) -> None:
#         print("BRD: oncheckbox clicked: ", checkbox.id)


# class SideBar(VerticalScroll):
#     def compose(self) -> ComposeResult:
#         yield Placeholder("Placeholder for P1", id="ph1")
#         yield Placeholder("Placeholder for P2", id="ph2")
#         yield Placeholder("Placeholder for P3", id="p3")
#         yield Checkbox("us-east-1 (iad)", id="iad")
#         iadCheck = RegionCheckBox("us-west-2", id="pdx")
#         #yield RegionCheckBox("us-west-2", id="pdx")
#         yield iadCheck

#     def on_checkbox_changed(sidebar):
#         print("BRD:   checkbox changed", sidebar)
        

#     def on_click(event):
#         print("BRD: Onclick: ", event)

# class ContentScreen(Container):
#     def compose(self) -> ComposeResult:
#         yield Placeholder("Delete unused S3 buckets", id="phc1", classes="phc")
#         yield Placeholder("Cloudwatch logs", id="phc2", classes="phc")
#         yield Placeholder("Cloudwatch logs", id="phc3", classes="phc")
#         yield Placeholder("Cloudwatch logs", id="phc4", classes="phc")
#         yield Placeholder("Cloudwatch logs", id="phc5", classes="phc")



# class MainScreen(Screen):
#     sideBar = None
#     content = None

#     def compose(self) -> ComposeResult:
#         yield Header("ToolBox")
#         yield Footer()
#         self.sideBar = SideBar(id="left-sidebar")
#         yield self.sideBar
#         self.content = ContentScreen(id="content-area")
#         yield self.content


class CWLogsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("A temporary placeholder")
        yield Placeholder("A temporary placeholder")

       

class MainApp(App):
    CSS_PATH = "main.tcss"
    SCREENS = {"main": mainScreen.MainScreen(id="main-screen"),
               "cwlogs": CWLogsScreen(id="cwlogs-screen") } 
    BINDINGS=[("m", "switch_screen('main')", "MainScreen"),
               ("c", "switch_screen('cwlogs')", "CWLogsScreen")]
    
    def on_mount(self) -> None:
        self.push_screen(mainScreen.MainScreen(id="main-screen"))


def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()
