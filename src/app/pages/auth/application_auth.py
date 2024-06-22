import flet as flet_app
from src.settings.application_settings import ApplicationSettings
from src.settings.registration_page_settings import RegistrationComponentsSettings
from src.app.components.field.registration_field import registration_field
#from src.app.components.button.reg_button import reg_outline_button
from src.app.components.button.reg_button import OutlineButton
from src.app.pages.auth.applicatin_registration import RegistrationPage
from flet import MainAxisAlignment
from flet_route import Params, Basket


class AuthenticationPage:

    def view(self, page: flet_app.Page, params: Params, basket: Basket):
        page.window_width = ApplicationSettings.weight_application
        page.window_height = ApplicationSettings.height_application
        page.window_resizable = ApplicationSettings.resizable_window
        page.title = ApplicationSettings.title_application

        return flet_app.View(
            "/",
            controls=[
                flet_app.Container(
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
                                        text="Войти",
                                        width=150,
                                        color="blue",
                                        to_page="Вход",
                                        page_now=page
                                    ).get_btn(),
                                    OutlineButton(
                                        text="Регистрация",
                                        width=150,
                                        color="blue",
                                        to_page="Регистрация",
                                        page_now=page
                                    ).get_btn()
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
            ]
        )