#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder, Collapsible, Button, Input, Header, Footer
from textual.containers import Container, VerticalScroll
import app1libs.environments as environments                                                                                                                                                            


class RegionSelectButton(Button):
    toggleOn = False
    def on_button_pressed(self, event) -> None:
        print("BRD: on toggle button ", type(event))
        if not self.toggleOn:
            self.toggleOn = True
            self.classes = "btnToggleOn"
        else:
            self.toggleOn = False
            self.classes = "btnToggleOff"


class RegionSelector(Collapsible):    
    envObjs = []
    def compose(self) -> ComposeResult:
        envObj = environments.Environments(envFile="./configs/environments.json")
        awsEnvs = envObj.getAwsEnvironments()
    
        with Collapsible(title="Environment Selection", 
                         classes="collapse01", collapsed=True):
            for env in awsEnvs:
                envString = "%s (%s)" %\
                    (envObj.getAwsEnvironmentRegion(env),envObj.getAwsEnvironmentProfile(env))
                obj = RegionSelectButton(envString, id=env, classes="btnToggleOff")
                self.envObjs.append(obj)
                yield obj


class SideMenuBar(VerticalScroll):
    def compose(self) -> ComposeResult:
        self.regionSelector = RegionSelector()
        yield self.regionSelector


class FilterInputArea(Container):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Logs Insight filter string")
        yield Button("Submit")

class ResultArea(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Placeholder("Placeholder for results", id="results")

        


class ContentArea(Container):
    def compose(self) -> ComposeResult:
        yield FilterInputArea(id="filterInputArea")
        yield ResultArea(id="resultArea")
        yield Placeholder("Placeholder for P1", id="ph1")
        yield Placeholder("Placeholder for P2", id="ph2")
        yield Placeholder("Placeholder for P3", id="p3")

   
class CWLogsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

        self.sideMenubar = SideMenuBar(id="sideMenuBar")
        yield(self.sideMenubar)
        self.contentScreen = ContentArea(id="contentArea")
        yield(self.contentScreen)
