#Other
from flet import (
    FilledTonalButton,
    ButtonStyle,
    TextField,
    AlertDialog,
    Text,
    Page,
    Column,
    colors
)


#Local
from src.app.components.bottom_sheet.bottom_sheet import BottomSheetForError
from src.app.components.field.registration_field import RegistrationField
from src.settings.application_settings import ApplicationSettings
from src.session import UserSession
from src.db.services.user_service import UserService


class DialogUpdateUserName:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.field_for_name: TextField = RegistrationField(text="Новое имя", width=ApplicationSettings.field_width+100).get_field()
        self.dialog_to_update_username: AlertDialog = AlertDialog(
            modal=True,
            title=Text(value="Обновление пользовательского имени"),
            content=Column(
                controls=[
                    self.field_for_name,
                    FilledTonalButton(
                        text="Обновить имя",
                        style=ButtonStyle(
                            bgcolor=colors.GREEN_ACCENT_400,
                            color=colors.BLACK
                        ),
                        width=ApplicationSettings.field_width + 100,
                        on_click=self.change_username
                    )
                ],
                height=100
            ),
            actions=[
                FilledTonalButton(
                    text="Закрыть",
                    on_click=lambda _: self.page.close(self.dialog_to_update_username),
                )
            ],
        )

    def change_username(self, e) -> None:
        """
        Обновление пользовательского имени
        :param e:
        :return:
        """

        if self.field_for_name.value:
            is_updated: bool = UserService().update_information(
                find_data={"_id": UserSession.id_user},
                data_update={"$set": {"username": self.field_for_name.value}}
            )
            if not is_updated:
                self.page.open(BottomSheetForError(text="Не удалось обновить ваше имя").get_bottom_sheet())
            self.page.close(self.dialog_to_update_username)

    def get_dialog_change_name(self) -> AlertDialog:
        return self.dialog_to_update_username