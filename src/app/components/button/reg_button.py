#System
from typing import Union


#Other libraries
import flet
import pydantic
from flet import OutlinedButton, ButtonStyle, app, TextField, Text, Row, MainAxisAlignment, Dropdown, FontWeight


#Local
from src.auth.auth import Authentication
from src.db.dto.user_dto import AddNewUser
from src.app.components.text.text_error import TextError
from src.api.crypt.coin_value import CoinValue
from src.api.currencies.course_value import CourseValue


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
            error: Text = None,
            dr_1: Dropdown = None,
            dr_2: Dropdown = None,
            field_1: TextField = None,
            field_2: TextField = None
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
        self.dr_1: Dropdown = dr_1
        self.dr_2: Dropdown = dr_2
        self.field_1 = field_1
        self.field_2 = field_2
        self.course_api = CourseValue()
        self.coin_api = CoinValue()

        if field_email and field_password:
            self.field_email: Union[None, TextField] = field_email
            self.field_password: Union[None, TextField] = field_password

    def continue_to_page(self, e):
        if self.to_page == "Конвертация валют":
            try:
                #Запрос на конвертацию
                result_convert: Union[float, None] = self.course_api.convert_value(
                    value_1=self.dr_1.value,
                    value_2=self.dr_2.value,
                    amount=int(self.field_1.value))

                if result_convert:
                    self.field_2.value = result_convert
                    self.error.value = (f"Валюта '{self.dr_1.value}' в сумме {self.field_1.value} успешно преобразовалась "
                                    f"в валюту '{self.dr_2.value}' на сумму {self.field_2.value}")
                    self.error.color = "green"
                    return

                raise ValueError("Ошибка конвертации")

            except Exception as ex:
                self.error.value = "Не удалось преобразовать валюту!"
                self.error.color = "red"
                self.error.weight = FontWeight.BOLD
            finally:
                self.page.update()
                return

        if self.to_page == "Конвертация криптовалюты":

            #Конвертация криптовалюты
            if self.field_1.value.isdigit():
                convert: Union[float, None] = self.coin_api.convert_crypt_to_usd(
                    value=int(self.field_1.value), crypt_name=self.dr_1.value
                )

                if convert:
                    self.field_2.value = convert
                    self.error.value = (f"Валюта '{self.dr_1.value}' в сумме {self.field_1.value} успешно преобразовалась "
                                        f"в валюту 'USD' на сумму {self.field_2.value}")
                    self.error.color = "green"
            else:
                self.error.value = "Не удалось конвертировать!"
                self.error.color = "red"

            self.page.update()

            return

        if self.to_page == "Вход":
            try:
                is_user: bool = Authentication().auth_user(user_data=AddNewUser(
                    email=self.field_email.value,
                    password=self.field_password.value
                ))
            except pydantic.ValidationError:
                self.error.value = "Неверное введённые данные!"
                self.page.update()
            else:
                if is_user:
                    self.page.go("/general")
                else:
                    self.error.value = "Неверные данные!"
                    self.page.update()
        else:
            if self.to_page == "Процесс регистрации":
                try:
                    create_user: bool = Authentication().user_is_created(user_data=AddNewUser(
                        email=self.field_email.value,
                        password=self.field_password.value
                    ))
                except pydantic.ValidationError:
                    self.error.value = "Неверное введённые данные!"
                    self.page.update()
                else:
                    if create_user is True:
                        self.page.go("/")
                    else:
                        self.error.value = "Данный пользователь уже зарегистрирован!"
                        self.page.update()
            else:
                self.page.go("/registration")

    def get_btn(self) -> OutlinedButton:
        return self.btn