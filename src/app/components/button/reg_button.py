from typing import Union

import flet
from flet import OutlinedButton, ButtonStyle, app
from src.app.pages.auth.application_auth import AuthenticationPage
from src.app.pages.auth.applicatin_registration import RegistrationPage


class OutlineButton:

    def __init__(self, text: str, width: int, color: str, to_page: flet.Page, page_now: flet.Page):
        self.btn = OutlinedButton(
            text=text,
            width=width,
            style=ButtonStyle(
                color=color
            )
        )
        self.page = page_now
        self.to_page = AuthenticationPage(flet.Page) if to_page == "Вход" else RegistrationPage(flet.Page)
        self.btn.on_click = self.continue_to_page

    def continue_to_page(self, e):
        self.page.clean()
        self.to_page.update()

    def get_btn(self) -> OutlinedButton:
        return self.btn