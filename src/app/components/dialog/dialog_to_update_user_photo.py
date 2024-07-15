#Other
import shutil
from flet import (
    AlertDialog,
    Page,
    Text,
    FilledTonalButton,
    FilePicker,
    Column,
    FilePickerResultEvent,
    FilePickerUploadFile,
    ButtonStyle
)
from bson.objectid import ObjectId


#Local
from src.session import UserSession
from src.settings.application_settings import ApplicationSettings
from src.db.services.user_service import UserService


class DialogUpdateUserPhoto:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.session: ObjectId = UserSession.id_user
        self.file_picker: FilePicker = FilePicker(
            on_result=self.save_file
        )
        self.page.overlay.append(
            self.file_picker
        )
        self.dialog_update_user_photo: AlertDialog = AlertDialog(
            modal=True,
            title=Text(value="Обновление вашей фотографии"),
            content=Column(
                controls=[
                    FilledTonalButton(
                        text="Выбрать фотографию",
                        on_click=lambda _: self.file_picker.pick_files(allow_multiple=True),
                        style=ButtonStyle(
                            color=ApplicationSettings.bd_color_outl
                        ),
                        width=ApplicationSettings.width_outl_btn_2+200
                    )
                ],
                height=40
            ),
            actions=[
                FilledTonalButton(
                    text="Закрыть",
                    on_click=lambda x: self.page.close(self.dialog_update_user_photo)
                )
            ]
        )

    def save_file(self, e: FilePickerResultEvent):
        """
        Сохранение и обновление картинки
        :param e:
        :return:
        """

        if e.files:
            shutil.copy(
                e.files[0].path,
                f"src/static/images/{e.files[0].name}"
            )

            #Добавление картинки
            is_updated: bool = UserService().update_information(
                find_data={
                    "_id": UserSession.id_user
                },
                data_update={
                    "$set": {
                        "photo_user": f"src/static/images/{e.files[0].name}"
                    }
                }
            )

            if is_updated:
                self.page.close(self.dialog_update_user_photo)

    def get_update_photo_dialog(self) -> AlertDialog:
        return self.dialog_update_user_photo
