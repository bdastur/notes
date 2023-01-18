#!/usr/bin/env python
# -*- coding: utf-8 -*-


#----------------------------------------------------------
# You can set window size programatically like below
# Also configure to disable/enable (default enabled) resizing.  
# Note: This import and congiuration should be before any other 
#       to take effect
from kivy.config import Config

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540') # 16:9
Config.set('graphics', 'resizable', 1)

# Disable the mouse right-click multitouch available on desktops
Config.set('input', 'mouse', 'mouse,disable_multitouch')

#----------------------------------------------------------

from kivy.app import App
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import kivy.graphics as kvgraphics

KV = """
#:import C kivy.utils.get_color_from_hex

<CanvasWidget>:
    clearButton: _clearButton
    Button:
        id: _clearButton
        text: "Delete"
        color: kivy.utils.get_color_from_hex("#0933F7")
        right: root.right 
        top: root.top
        width: 120
        height: 80
    BoxLayout:
        orientation: "horizontal"
        padding: 3
        spacing: 3
        x: 0
        y: 0
        width: root.width
        height: 40

        ToggleButton:
            group: "color"
            text: "Red"
            background_color: C("#E74C3C")
            on_press: app.canvasWidget.setColor(C("#E74C3C"))
        ToggleButton:
            group: "color"
            text: "Blue"
            background_color: C("#3498DB")
            on_press: app.canvasWidget.setColor(C("#3498DB"))
            state: "down"
    BoxLayout:
        orientation: "vertical"
        padding: 3
        spacing: 3
        x: 0
        top: root.top
        width: 140
        height: 120
        ToggleButton:
            group: "line_width"
            text: "Thin"
            on_press: app.canvasWidget.setLineWidth("Thin")
        ToggleButton:
            group: "line_width"
            text: "Medium"
            on_press: app.canvasWidget.setLineWidth("Medium")
        ToggleButton:
            group: "line_width"
            text: "Thick"
            on_press: app.canvasWidget.setLineWidth("Thick")
"""
Builder.load_string(KV)



class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self.lineWidth = 2
    
    def on_touch_down(self, touch):
        print(touch.x, touch.y)
        if Widget.on_touch_down(self, touch):
            print("Return here.")
            #self.clearCanvas()
            return

        with self.canvas:        
            #kvgraphics.Color(*get_color_from_hex("#3c804e"))
            # (older less elegant) kvgraphics.Line(circle=(touch.x, touch.y, 25), width=4)
            touch.ud["current_line"] = kvgraphics.Line(
                points=(touch.x, touch.y), width=self.lineWidth)
    
    def setColor(self, newColor):
        self.lastColor = newColor
        self.canvas.add(kvgraphics.Color(*newColor))
    
    def setLineWidth(self, newWidth="Medium"):
        widths = {
            'Thin': 1, 'Medium': 2, 'Thick': 4
        }
        self.lineWidth = widths[newWidth]
    

    def on_touch_move(self, touch):
        # Older less elegant using circle
        #with self.canvas:        
        #    kvgraphics.Color(*get_color_from_hex("#3c804e"))
        #    kvgraphics.Line(circle=(touch.x, touch.y, 25), width=4)
        if "current_line" in touch.ud:
            touch.ud["current_line"].points += (touch.x, touch.y)
          

    def clearCanvas(self):
        # The [:] expression is an array copy. If we used 
        # savedChildred = self.children, this means we are copying a pointer
        # to the array. When we call self.clear_widgets(), it will remove
        # everything from both self.children and savedChildren
        savedChildren = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in savedChildren:
            self.add_widget(widget)
        self.setColor(self.lastColor)
        self.setLineWidth(newWidth='Normal')




class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        
        self.canvasWidget = CanvasWidget()
        self.canvasWidget.setColor(get_color_from_hex("#3517cf"))
        return self.canvasWidget


def main():
    Window.clearcolor = get_color_from_hex("#FFFFFF")
    PaintApp().run()


if __name__ == '__main__':
    main()


