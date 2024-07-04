#System
from typing import Union


#Other libraries
import flet
import pydantic
from bson.objectid import ObjectId
from flet import OutlinedButton, ButtonStyle, app, TextField, Text, Row, MainAxisAlignment, Dropdown, FontWeight


#Local
from src.auth.auth import Authentication
from src.db.dto.user_dto import AddNewUser
from src.db.dto.history_dto import AddHistory
from src.app.components.text.text_error import TextError
from src.session import UserSession
from src.api.crypt.coin_value import CoinValue
from src.app.components.bottom_sheet.bottom_sheet import BottomSheetForError
from src.api.currencies.course_value import CourseValue
from src.db.services.user_service import UserService
from src.db.services.history_service import HistoryService


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
            remember: flet.Checkbox = None,
            dr_1: Dropdown = None,
            dr_2: Dropdown = None,
            field_1: TextField = None,
            field_2: TextField = None,
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
        self.remember = remember
        self.course_api = CourseValue()
        self.coin_api = CoinValue()
        self.user_service: UserService = UserService()
        self.history_service: HistoryService = HistoryService()

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

                    #Обновление информации о пользователе
                    self.user_service.update_information(
                        find_data={"_id": ObjectId(UserSession.id_user)},
                        data_update={"$inc": {"count_convert_value": 1, "count_general_convert": 1}}
                    )

                    #Добавление истории
                    self.history_service.add_new(
                        new_history=AddHistory(
                            user_id=UserSession.id_user,
                            from_operation=self.dr_1.value,
                            to_operation=self.dr_2.value
                        )
                    )
                    self.field_2.value = result_convert
                    return

                raise ValueError("Ошибка конвертации")

            except Exception as ex:
                bottom_sheet: BottomSheetForError = BottomSheetForError(page=self.page)
                self.page.open(bottom_sheet.get_bottom_sheet())
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
                    #Обновление данных
                    self.user_service.update_information(
                        find_data={"_id": ObjectId(UserSession.id_user)},
                        data_update={"$inc": {"count_general_convert": 1, "count_convert_coin": 1}}
                    )

                    #Добавление истории
                    self.history_service.add_new(
                        new_history=AddHistory(
                            user_id=UserSession.id_user,
                            from_operation=self.dr_1.value,
                            to_operation="USD"
                        )
                    )
                    self.field_2.value = convert
            else:
                bottom_sheet: BottomSheetForError = BottomSheetForError(page=self.page)
                self.page.open(bottom_sheet.get_bottom_sheet())

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

                    #Set id for local session
                    UserSession.id_user = is_user

                    if self.remember.value is True:
                        with open("user_data.txt", "w", encoding="UTF-8") as file:
                            file.write(self.field_email.value+"\n"+self.field_password.value)
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