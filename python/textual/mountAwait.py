#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textual.app import App, ComposeResult
from textual.widgets import Button, Welcome


class WelcomeApp(App):

    # make this function an async function.
    async def on_key(self) -> None:
        # here we want to await the result of mount() before we proceed to
        # change the button label.
        await self.mount(Welcome())
        self.query_one(Button).label = "YES!"

    def on_button_pressed(self) -> None:
        self.exit()


def main():
    app = WelcomeApp()
    app.run()

if __name__ == '__main__':
    main()

