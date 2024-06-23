import flet as flet_app
from src.settings.application_settings import ApplicationSettings
from src.settings.registration_page_settings import RegistrationComponentsSettings
from src.app.components.field.registration_field import RegistrationField
from src.app.components.button.reg_button import OutlineButton
from flet import MainAxisAlignment
from flet_route import Params, Basket


class AuthenticationPage:

    def view(self, page: flet_app.Page, params: Params, basket: Basket):
        page.window_width = ApplicationSettings.weight_application
        page.window_height = ApplicationSettings.height_application
        page.window_resizable = ApplicationSettings.resizable_window
        page.title = ApplicationSettings.title_application

        email_field = RegistrationField(text="Почта", width=RegistrationComponentsSettings.field_width).get_field()
        password_field = RegistrationField(text="Пароль", width=RegistrationComponentsSettings.field_width).get_field()

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
                            email_field,
                            password_field,
                            flet_app.Row(
                                controls=[
                                    OutlineButton(
                                        text="Войти",
                                        width=150,
                                        color="blue",
                                        to_page="Вход",
                                        page_now=page,
                                        field_email=email_field,
                                        field_password=password_field
                                    ).get_btn(),
                                    OutlineButton(
                                        text="Регистрация",
                                        width=150,
                                        color="blue",
                                        to_page="Регистрация",
                                        page_now=page,
                                        field_email=email_field,
                                        field_password=password_field
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