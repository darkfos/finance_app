import flet as flet_app
from src.settings.application_settings import ApplicationSettings
from src.settings.registration_page_settings import RegistrationComponentsSettings
from src.app.components.field.registration_field import registration_field
from src.app.components.button.reg_button import OutlineButton
from src.app.pages.auth.application_auth import AuthenticationPage
from flet import MainAxisAlignment


class RegistrationPage:

    def __init__(self, page: flet_app.Page):
        self.page = page
        self.page.window_width = ApplicationSettings.weight_application
        self.page.window_height = ApplicationSettings.height_application
        self.page.window_resizable = ApplicationSettings.resizable_window
        self.page.title = ApplicationSettings.title_application

        self.set_components()
        self.update()

    def update(self):
        """
        Обновление страницы
        :return:
        """

        self.page.update()

    def set_components(self):
        """
        Установка компонентов
        :return:
        """

        auth_container = flet_app.Container(
            flet_app.Column(
                controls=[
                    flet_app.Image(
                        src="/home/darkfos/PycharmProjects/finance_app/src/static/images/logo.png",
                        width=ApplicationSettings.weight_application,
                        height=100,
                    ),
                    registration_field(text="Почта", width=RegistrationComponentsSettings.field_width),
                    registration_field(text="Пароль", width=RegistrationComponentsSettings.field_width),
                    flet_app.Row(
                        controls=[
                            OutlineButton(
                                text="Зарегистрироваться",
                                width=150,
                                color="blue",
                                page_now=self.page,
                                to_page="Вход"
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
                spacing=15
            ),
            margin=flet_app.margin.only(
                left=ApplicationSettings.weight_application // 4,
                right=ApplicationSettings.weight_application // 4,
                top=150
            )
        )

        self.page.add(auth_container)
