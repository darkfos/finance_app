from typing import Union
import flet
from flet import OutlinedButton, ButtonStyle, app, TextField, Text, Row, MainAxisAlignment
from src.auth.auth import Authentication
from src.db.dto.user_dto import AddNewUser
from src.app.components.text.text_error import TextError


class OutlineButton:

    def __init__(
            self,
            text: str,
            width: int,
            color: str,
            to_page: Union["Вход", "Регистрация"],
            page_now: flet.Page,
            field_email: Union[None, TextField] = None,
            field_password: Union[None, TextField] = None,
            error: Text = None
    ):
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
        self.error = error

        if field_email and field_password:
            self.field_email: Union[None, TextField] = field_email
            self.field_password: Union[None, TextField] = field_password

    def continue_to_page(self, e):
        if self.to_page == "Вход":
            self.page.go("/")
        else:
            if self.to_page == "Процесс регистрации":
                create_user: bool = Authentication().user_is_created(user_data=AddNewUser(
                    email=self.field_email.value,
                    password=self.field_password.value
                ))
                if create_user is True:
                    self.page.go("/")
                else:
                    self.error.value = "Данный пользователь уже зарегистрирован!"
                    self.page.update()
            else:
                self.page.go("/registration")

    def get_btn(self) -> OutlinedButton:
        return self.btn