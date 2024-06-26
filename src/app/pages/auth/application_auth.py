#Other libraries
import flet as flet_app
from flet import View
from flet import MainAxisAlignment, icons
from flet_route import Params, Basket

#Local
from src.settings.application_settings import ApplicationSettings
from src.app.components.field.registration_field import RegistrationField
from src.app.components.button.reg_button import OutlineButton
from src.app.components.text.text_error import TextError
from src.app.components.chech_box.checkbox_reg import CheckBoxReg
from src.app.pages.page_fabric import PageFabric


class AuthenticationPage(PageFabric):

    def __init__(self):
        self.view_authentication: View = View(route="/")

    def set_components(self):
        email_field = RegistrationField(
            text="Почта",
            width=ApplicationSettings.field_width,
            icon=icons.EMAIL
        ).get_field()
        password_field = RegistrationField(
            text="Пароль",
            width=ApplicationSettings.field_width,
            password=True,
            icon=icons.PASSWORD
        ).get_field()
        check_box_show_password: flet_app.Checkbox = CheckBoxReg(
            text="Показать пароль",
            page=self.page,
            field=password_field
        ).get_check_box()
        text_error = TextError(txt="").get_text_error()

        self.view_authentication.controls = [
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
                        check_box_show_password,
                        flet_app.Row(
                            controls=[
                                OutlineButton(
                                    text="Войти",
                                    width=ApplicationSettings().width_outl_btn_2,
                                    color=ApplicationSettings().bd_color_outl,
                                    to_page="Вход",
                                    page_now=self.page,
                                    field_email=email_field,
                                    field_password=password_field,
                                    error=text_error
                                ).get_btn(),
                                OutlineButton(
                                    text="Регистрация",
                                    width=ApplicationSettings().width_outl_btn_2,
                                    color=ApplicationSettings().bd_color_outl,
                                    to_page="Регистрация",
                                    page_now=self.page,
                                    field_email=email_field,
                                    field_password=password_field,
                                    error=text_error,
                                ).get_btn()
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        flet_app.Row(
                            controls=[
                                text_error
                            ],
                            alignment=MainAxisAlignment.CENTER
                        )
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

    def view(self, page: flet_app.Page, params: Params, basket: Basket):

        self.page = page
        self.page.window_width = ApplicationSettings.weight_application
        self.page.window_height = ApplicationSettings.height_application
        self.page.window_resizable = ApplicationSettings.resizable_window
        self.page.title = ApplicationSettings.title_application

        #Установка компонентов
        self.set_components()

        return self.view_authentication