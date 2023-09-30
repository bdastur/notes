#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button

class ToggleButton(Button):
    toggleOn=False
    def on_button_pressed(self, event) -> None:
        print("BRD: on toggle button pressed: ", event)
        if not self.toggleOn:
            self.toggleOn = True
            self.classes = "toggleOn"
        else:
            self.toggleOn = False
            self.classes = ""


class MainApp(App):
    CSS_PATH="./buttons01.tcss"
    def compose(self) -> ComposeResult:
        yield Button("Test Button", id="btn1")
        yield ToggleButton("Toggle Test Button", id="tbtn1")
        yield ToggleButton("Toggle Test Button", id="tbtn2")
        yield ToggleButton("Toggle Test Button", id="tbtn3")
        yield ToggleButton("Toggle Test Button", id="tbtn4")

    
    

def main():
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()
