# Kivy

## Links:
* [Kivy framework](https://kivy.org/doc/stable/gettingstarted/events.html)
* [A mobile app with Kivy](https://realpython.com/mobile-app-kivy-python/#using-the-kv-language)
* [Kivy tutorial](https://www.geeksforgeeks.org/python-checkbox-widget-in-kivy/)
* [Buildozer Docker repo](https://github.com/kivy/buildozer/blob/master/Dockerfile)
* [Kivy tutorial](https://www.netguru.com/blog/building-cross-platform-gui-applications-in-kivy)
* [KivyMD tutorial - github](https://github.com/attreyabhatt/KivyMD-Basics)
* [KivyMD - Github](https://github.com/kivymd/KivyMD)
* [KivyMD - components github wiki](https://github.com/kivymd/KivyMD/wiki)

resorces to learn kivy python

1. Kivy Tutorials:
https://kivy.org/doc/stable/tutorials/index.html

2. Kivy Documentation:
https://kivy.org/doc/stable/

3. Kivy Cookbook:
https://kivy.org/doc/stable/cookbook/

4. Kivy Crash Course:
https://www.youtube.com/watch?v=F7UKmK9eQLw

5. Kivy Tutorials for Beginners:
https://www.youtube.com/watch?v=HVV3JfFjxkQ


7. Real Python Kivy Tutorial:
https://realpython.com/mobile-app-kivy-python/


8. Kivy with Python Tutorials:
https://www.tutorialspoint.com/kivy/index.htm


## How to's and tips.

### Using Object property.
Its clean to keep the presentation part in .kv file. You can reference the widgets and
properties defined in .kv file using ObjectProperty.

Eg of how to do that below:

.kv fle:
```
<CustomPageLaout>
    button1: _oneButton
    button2: _twoButton

    Button:
        id: _oneButton
        text: "test button"
    Button:
        id: _twoButton
        text: "test two button"
   
```

.py file:
```
from kivy.uix.pagelayout import PageLayout
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_file("./page_layout.kv")

class CustomPageLayout(PageLayout):
    def __init__(self, **kwargs):
        super(CustomPageLayout, self).__init__(**kwargs)
        button3 = ObjectProperty()
        :

        self.button3.text = "Object property change"
        
```

Here you can reference the button with id '\_twoButton', using the object property.



### Converting hex color to kivy format [ratio, ratio, ratio, 1]

Using the get_color_from_hex() API.
```
<CustomButton@Button>
    color: kivy.utils.get_color_from_hex("#7feb8d")
```

