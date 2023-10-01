#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal, VerticalScroll, ScrollableContainer
from textual.widgets import Header, Static, Placeholder, Input, Label, Button, Collapsible
import app1libs.environments as environments                                                                                                                                                            


class RegionSelectButton(Button):
    toggleOn = False

    def on_mount(self):
        self.originalLabel = self.label;
    
    def on_button_pressed(self, event) -> None:
        print("BRD: on toggle button ", type(event))
        if not self.toggleOn:
            self.toggleOn = True
            self.classes = "btnToggleOn"
            self.label += " (Selected)"
        else:
            self.toggleOn = False
            self.classes = "btnToggleOff"
            self.label = self.originalLabel;
        print(self.label)

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
        self.regionSelector = RegionSelector(id="regionSelector")
        yield self.regionSelector
        yield Placeholder("Menu item one", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")
        yield Placeholder("Menu item two", classes="menuItems")



class InputArea(Container):
    def compose(self) -> ComposeResult:
        self.input = Input(placeholder="Text input", id="input01")
        yield self.input
        self.submitButton = Button("Submit", id="button01")
        yield self.submitButton


class ResultArea(ScrollableContainer):
    def compose(self) -> ComposeResult:
        yield Collapsible(title="Results are here, and a long text")
        yield Placeholder("Result Item one", classes="resultItems")
        yield Placeholder("Result Item two", classes="resultItems")
        yield Placeholder("Result Item three", classes="resultItems")
        yield Placeholder("Result Item four", classes="resultItems")
        yield Placeholder("Result Item five", classes="resultItems")
        yield Placeholder("Result Item six", classes="resultItems")
        yield Placeholder("Result Item seven", classes="resultItems")
        yield Placeholder("Result Item eight", classes="resultItems")
        yield Placeholder("Result Item nine", classes="resultItems")
        # Note that since Result area is a grid, it does not scroll. 
        # we should probably put this within a vertical scroll
        yield Placeholder("Result Item ten", classes="resultItems")
        yield Placeholder("Result Item eleven", classes="resultItems")
        yield Placeholder("Result Item twelve", classes="resultItems")



class ContentArea(Container):
    def compose(self) -> ComposeResult:
        yield InputArea(id="inputArea")
        yield ResultArea(id="resultArea")


class CWLogsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield SideMenuBar(id="sideMenubar")
        yield ContentArea(id="contentArea")


class MainApp(App):
    CSS_PATH = "cwlogs.tcss"
    def on_mount(self) -> None:
        self.push_screen(CWLogsScreen(id="cwLogsScreen"))


def main():
    mainApp = MainApp()
    mainApp.run()

if __name__ == '__main__':
    main()
