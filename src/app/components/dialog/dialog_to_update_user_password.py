#Other
from flet import (
    AlertDialog,
    Page,
    Text,
    FilledTonalButton,
    Column,
    ButtonStyle,
    TextField,
    colors
)


#Local
from src.session import UserSession
from src.auth.hash import HashService
from src.db.services.user_service import UserService
from src.app.components.field.registration_field import RegistrationField
from src.app.components.bottom_sheet.bottom_sheet import BottomSheetForError
from src.settings.application_settings import ApplicationSettings


class DialogUpdateUserPassword:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.field_password_1: TextField = RegistrationField(text="Старый пароль", width=ApplicationSettings.field_width + 80).get_field()
        self.field_password_2: TextField = RegistrationField(text="Новый пароль", width=ApplicationSettings.field_width + 80).get_field()

        self.dialog_update_user_password: AlertDialog = AlertDialog(
            modal=True,
            title=Text(value="Обновление пароля"),
            content=Column(
                controls=[
                    self.field_password_1,
                    self.field_password_2,
                    FilledTonalButton(
                        text="Изменить пароль",
                        width=ApplicationSettings.field_width + 80,
                        on_click=self.change_password,
                        style=ButtonStyle(
                            bgcolor=colors.GREEN_ACCENT_400,
                        )
                    )
                ],
                height=140
            ),
            actions=[
                FilledTonalButton(
                    text="Закрыть",
                    on_click=lambda _: self.page.close(self.dialog_update_user_password)
                )
            ]
        )

    def change_password(self, e) -> None:
        """
        Обновление пароля
        :param e:
        :return:
        """

        if self.field_password_1.value and self.field_password_2.value:
            user_data: dict = UserService().get_one(id_user=UserSession.id_user)
            hash_password = HashService().verify(
                password_found=user_data.get("password"),
                user_password=self.field_password_1.value
            )

            if hash_password:
                #Обновление пароля
                is_updated: bool = UserService().update_information(
                    find_data={"_id": UserSession.id_user},
                    data_update={"$set": {
                        "password": str(HashService().hash_password(password=self.field_password_2.value))
                    }}
                )

                if is_updated:
                    self.page.close(self.dialog_update_user_password)
            else:
                self.page.close(self.dialog_update_user_password)
                self.page.open(
                    BottomSheetForError(
                        page=self.page,
                        text="Не удалось обновить пароль!"
                    ).get_bottom_sheet()
                )

    def get_dialog(self) -> AlertDialog:
        return self.dialog_update_user_password