#System
from typing import Union

from flet import TextField, icons


class RegistrationField:

    def __init__(self, text: str, width: int, password: bool = False, disable_field: bool = False, icon: icons = None):
        self.field = TextField(label=text, width=width, password=password, disabled=disable_field)
        if icon:
            self.field.icon = icon

    def get_field(self) -> TextField:
        return self.field