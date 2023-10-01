#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.message import Message
from textual.color import Color
from textual.screen import Screen
from textual.containers import Container, VerticalScroll
from textual.widget import Widget
from textual.widgets import Checkbox, Placeholder, Header, \
                            Footer, Collapsible, Label, Button, Input

class InputHandler(Input):
    def on_key(self, event) -> None:
        print("On key: ", event)
        self.post_message(self.Selected(self.value))
    
    class Selected(Message):
        def __init__(self, msg) -> None:
            print("TextNotify msg: ", msg)
            self.value = msg
            super().__init__()
    

class ColorButton(Button):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()
    
    def on_mount(self) -> None:
        self.styles.margin = (1, 2)
        self.styles.background = Color.parse("#ffffff33")
        self.styles.border = ("tall", self.color)
    
    def on_click(self) -> None:
        print("ColorButton on_click")
        self.post_message(self.Selected(self.color))
    
    def render(self) -> None:
        #print("ColorButton render invoked!")
        return str(self.color)
    
    class Selected(Message):
        def __init__(self, color: Color) -> None:
            self.color = color
            super().__init__()


class ColorApp(App):
    def compose(self) -> ComposeResult:
        yield ColorButton(Color.parse("#080090"))
        yield ColorButton(Color.parse("#808000"))
        yield ColorButton(Color.parse("#E9967A"))
        yield ColorButton(Color.parse("#121212"))
        self.inputHandler = InputHandler(placeholder="Input text")
        yield self.inputHandler
    
    def on_color_button_selected(self, message: ColorButton.Selected) -> None:
        print("BRD: ColorApp on_color_button_Selected ", self.inputHandler.value)
        self.screen.styles.animate("background", message.color, duration=0.5)

    def on_input_handler_selected(self, msg: InputHandler.Selected) -> None:
        print("BRD: on_input_handler_textnotify ", msg.value)


def main():
    app = ColorApp()
    app.run()

if __name__ == '__main__':
    main()
