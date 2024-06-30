#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example which sets styles on screen (A widget that represents the screen)
"""

from textual.app import App, ComposeResult
from textual.widgets import Static
import textual.color as color
from textual.color import Color


class ScreenOne(App[str]):
    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"
        self.screen.styles.border = ("heavy", "white")
    
    def compose(self) -> ComposeResult:
        text = """
        I must not fear.
        Fear is the mind killer.
        Fear is the little-death that brings total obliteration.
        I will face my fear.
        I will permit it to pass over me and through me.
        And when it is gone past, I will turn the inner eye to see it's path.
        Where fear has gone there will be nothing. Only I will remain.
        """
        self.widget1 = Static(text)
        self.widget2 = Static(text)
        self.widget3 = Static(text)
        self.widget4 = Static(text)

        #################################################
        # Background color
        #################################################
        self.widget1.styles.background = "green"
        self.widget2.styles.background = Color.parse("mediumblue")

        # Textual represents color internally as a tuple of three values for
        # reg, green and blue. A fourth argument is called alpha that can make
        # the color translucent. Alpha is a flot from 0 to 1.0
        self.widget3.styles.background = Color(204, 143, 34, 0.3)
        self.widget4.styles.background = Color.parse("green")
        
        #################################################
        # Border
        #################################################
        self.widget1.styles.border = ("heavy", "white")
        # Border with title and subtitle
        self.widget1.border_title = "First Widget"
        self.widget1.border_subtitle = "with a border title and subtitle"
        self.widget1.styles.border_title_align = "left"

        # An outline is similar to border and is set the same way. Difference is,
        # an outline will not change the size of the widget, and may overlap
        # the content area.
        self.widget1.styles.outline = ("heavy", "yellow")

        self.widget2.styles.border = ("heavy", "lime")
        self.widget3.styles.border = ("heavy", "peachpuff")
        self.widget4.styles.border = ("heavy", "black")

        #################################################
        # Width & Height
        #################################################
        # Setting with to 50% in proportion to the widget's parent size.
        self.widget1.styles.width = "50%"
        self.widget1.styles.height = "auto"

        # Absolute units
        self.widget2.styles.width = 50
        self.widget2.styles.height = 10

        # FR units. Work when you use this for all widgets within the parent.
        # When specifying fr units textual will divide the available space by
        # the sum of the fr units on that dimension. The space will be divided
        # amongst the widgets as a proportion of their individual fr values.
        self.widget3.styles.width = "1fr"
        self.widget4.styles.width = "2fr"
        self.widget3.styles.height = "1fr"
        self.widget4.styles.height = "2fr"

        #################################################
        # Padding
        #################################################
        # Set padding to 6 for top/bottom and left/right
        self.widget1.styles.padding = 6

        # Set padding to 6 for top/bottom and 10 left/right
        self.widget2.styles.padding = (2, 4)

        yield self.widget1
        yield self.widget2
        yield self.widget3
        yield self.widget4
    

def main():
    app = ScreenOne()
    app.run()

if __name__ == '__main__':
    main()