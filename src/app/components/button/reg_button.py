from typing import Union
import flet
from flet import OutlinedButton, ButtonStyle, app


class OutlineButton:

    def __init__(self, text: str, width: int, color: str, to_page: Union["Вход", "Регистрация"], page_now: flet.Page):
        self.btn = OutlinedButton(
            text=text,
            width=width,
            style=ButtonStyle(
                color=color
            )
        )
        self.page = page_now
        self.to_page = to_page
        self.btn.on_click = self.continue_to_page

    def continue_to_page(self, e):

        if self.to_page == "Вход":
            self.page.go("/")
        else:
            self.page.go("/registration")

    def get_btn(self) -> OutlinedButton:
        return self.btn