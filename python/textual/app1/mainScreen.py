#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, VerticalScroll
from textual.widget import Widget
from textual.widgets import Checkbox, Placeholder, Header, \
                            Footer, Collapsible, Label, Button


class RegionSelectButton(Button):
    checked = False
    def on_click(self) -> None:
        print("BRD: REgion Select Button clicked", self.id)


class RegionCheckBox(Checkbox):
    checked = False 
    def on_click(self) -> None:
        print("BRD: here on click: ", self, self.id)
        self.checked = True

    def on_region_checkbox_changed(checkbox) -> None:
        print("BRD: oncheckbox clicked: ", checkbox.id)


class RegionSelector(Collapsible):
    checked = False
    environments = {
        "iad": {
            "region": "us-east-1",
            "profile": "iad",
            "account_id": 889222324512
        },
        "dev": {
            "region": "eu-west-1",
            "profile": "dev",
            "account_id": 112309893332
        }
    }

    envObjs = []

    def __init__(self) -> None:
        super().__init__()
        self.envObjs = []
   
    def compose(self) -> ComposeResult:
        with Collapsible(title="Environment Selection", 
                         classes="collapse01",
                         collapsed=True):
            for envId in self.environments:
                env = self.environments[envId]
                envString ="%s %s" % (env["region"], env["account_id"])
                obj = RegionCheckBox(envString, id=envId, classes="envCheckbox")
                self.envObjs.append(obj)
                yield obj
            yield RegionSelectButton(name="Regionfoo")
                
           
 

class SideBar(VerticalScroll):
   
    regionSelector = None
    def compose(self) -> ComposeResult:
        yield Placeholder("Placeholder for P1", id="ph1")
        yield Placeholder("Placeholder for P2", id="ph2")
        yield Placeholder("Placeholder for P3", id="p3")
        yield Collapsible(Label("Environment Selection"))
        self.regionSelector = RegionSelector()
        yield self.regionSelector
        yield Button(label="Submit")
        yield RegionSelectButton(label="Testing")
        

    def on_button_pressed(self, event: Button.Pressed):
        print("BRD: Button pressed: ", event.button.id)
        print("BRD Environments: ", self.regionSelector.envObjs, len(self.regionSelector.envObjs))
        for env in self.regionSelector.envObjs:
            print("Selected env: ", env.checked)


    def on_checkbox_changed(self, sidebar):
        print("BRD:  checkbox changed", sidebar)
        

    def on_click(self, event: Button.Pressed) -> None:
        print("BRD: Onclick: ", event.button)


class ContentScreen(Container):
    def compose(self) -> ComposeResult:
        yield Placeholder("Delete unused S3 buckets", id="phc1", classes="phc")
        yield Placeholder("Cloudwatch logs", id="phc2", classes="phc")
        yield Placeholder("Cloudwatch logs", id="phc3", classes="phc")
        yield Placeholder("Cloudwatch logs", id="phc4", classes="phc")
        yield Placeholder("Cloudwatch logs", id="phc5", classes="phc")



class MainScreen(Screen):
    sideBar = None
    content = None
    CSS_PATH = "main.tcss"

    def compose(self) -> ComposeResult:
        yield Header(name="ToolBox")
        yield Footer()
        self.sideBar = SideBar(id="left-sidebar")
        yield self.sideBar
        self.content = ContentScreen(id="content-area")
        yield self.content

