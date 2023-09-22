#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import monotonic
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import ScrollableContainer
from textual.reactive import reactive


class TimeDisplay(Static):
    """A Widget to display elapsed time"""

    startTime = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        #self.set_interval(1/60, self.update_time)
        self.update_timer = self.set_interval(1/60, self.update_time, pause=True)

    def update_time(self) -> None:
        #self.time = monotonic() - self.startTime
        self.time = self.total + (monotonic() - self.startTime)

    """
    If you implement a method that begins with watch_ followed by the name of 
    a reactive attribute, then the method will be called when the attribute is 
    modified. Such methods are known as watch methods.
    """
    def watch_time(self, time: float) -> None:
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        self.startTime = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        self.update_timer.pause()
        self.total += monotonic() - self.startTime
        self.time = self.total

    def reset(self) -> None:
        self.total = 0
        self.time = 0


class StopWatch(Static):
    """A stopwatch widget"""

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        buttonId = event.button.id
        timeDisplay = self.query_one(TimeDisplay)

        if buttonId == "start":
            timeDisplay.start()
            self.add_class("started")
        elif buttonId == "stop":
            timeDisplay.stop()
            self.remove_class("started")
        elif buttonId == "reset":
            timeDisplay.reset()


class StopWatchApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("ctrl+c", "quit", "Quit"),
                ("a", "add_stopwatch", "Add"),
                ("r", "remove_stopwatch", "Remove")]

    CSS_PATH = "stopwatch01.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(StopWatch(), StopWatch(), id="timers")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_add_stopwatch(self) -> None:
        newStopWatch = StopWatch()
        self.query_one("#timers").mount(newStopWatch)
        newStopWatch.scroll_visible()


def main() -> None:
    app = StopWatchApp()
    app.run()


if __name__ == '__main__':
    main()


