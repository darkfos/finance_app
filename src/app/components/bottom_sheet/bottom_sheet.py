#System
from typing import Union

#Other
from flet import (
    BottomSheet,
    OutlinedButton,
    Text,
    Column,
    FontWeight,
    Page,
    MainAxisAlignment,
    CrossAxisAlignment,
    Image,
    Container,
    transform,
    alignment,
    animation,
    AnimationCurve,
)


#Local
from src.settings.application_settings import ApplicationSettings


class BottomSheetForError:

    def __init__(self, page: Page, text: Union[str, None] = None):
        self.page = page
        self.app_settings: ApplicationSettings = ApplicationSettings()
        self.img = Image(
                src="/home/darkfos/PycharmProjects/finance_app/src/static/images/logo.png",
            )
        self.container_with_img: Container[Image] = Container(
            content=self.img,
            width=50,
            height=50,
            animate=animation.Animation(1000, AnimationCurve.BOUNCE_OUT),
        )
        self.bt_sheet: BottomSheet = BottomSheet(
            content=
                Column(
                    controls=[
                        self.container_with_img,
                        Text(
                            value=text if text else "Не удалось конвертировать валюту!",
                            color="red",
                            weight=FontWeight.BOLD,
                            size=18
                        ),
                        OutlinedButton(
                            text="Закрыть",
                            on_click=lambda btn: self.page.close(self.bt_sheet),
                            width=self.app_settings.width_outl_btn,
                            on_hover=self.animate_img
                        )
                    ],
                    width=self.app_settings.weight_application,
                    height=self.app_settings.height_application - 425,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                ),
            )

    def animate_img(self, e):
        """
        Анимация ошибки
        :param e:
        :return:
        """

        self.container_with_img.width = 70 if self.container_with_img.width == 50 else 50
        self.container_with_img.height = 70 if self.container_with_img.width == 50 else 50
        self.page.update()

    def get_bottom_sheet(self) -> BottomSheet:
        return self.bt_sheet