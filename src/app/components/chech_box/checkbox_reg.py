#System
from typing import Union


#Other libraries
from flet import Checkbox, TextField, Page


class CheckBoxReg:

    def __init__(
            self,
            text: str,
            page: Page,
            field: Union[TextField, None] = None,
    ):
        self.check_box: Checkbox = Checkbox(
            label=text,
            on_change=self.change_check_box,
        )
        self.field: TextField = field
        self.page: Page = page

    def change_check_box(self, e):
        """
        Событие при измении состояния чек бокса
        :param e:
        :return:
        """

        if self.field:
            if self.field.password is True:
                self.field.password = False
            else:
                self.field.password = True
        self.page.update()

    def get_check_box(self) -> Checkbox:
        return self.check_box