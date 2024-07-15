#System
from typing import Union


#Other libraries
from flet import FilledTonalButton, Page, ButtonStyle


class FilledTonalButtonReg:

    def __init__(self, text: str, page: Page, bg: Union[None, str] = False, color: Union[None, str] = None,
                 on_click = None):
        self.btn: FilledTonalButton = FilledTonalButton(
            text=text,
            on_click=on_click if on_click else self.go_to_general_page,
            style=ButtonStyle(
                bgcolor=bg,
                color=color
            )
        )
        self.page = page

    def go_to_general_page(self, e):
        """
        Переход на главную страницу
        :param e:
        :return:
        """

        self.page.go("/")

    def get_filled_tonal_btn(self) -> FilledTonalButton:
        return self.btn