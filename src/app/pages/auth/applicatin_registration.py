#Other libraries
import flet as flet_app
from flet import View
from flet import MainAxisAlignment, icons
from flet_route import Basket, Params


#Local
from src.settings.application_settings import ApplicationSettings
from src.app.components.field.registration_field import RegistrationField
from src.app.components.text.text_error import TextError
from src.app.components.button.reg_button import OutlineButton
from src.app.components.chech_box.checkbox_reg import CheckBoxReg, Checkbox
from src.app.components.button.filled_tonal_button_reg import FilledTonalButtonReg, FilledTonalButton
from src.app.pages.page_fabric import PageFabric


class RegistrationPage(PageFabric):

    def __init__(self):
        self.view_registration: View = View(route="/registration")

    def set_components(self):
        btn_gnr: FilledTonalButton = FilledTonalButtonReg(
            text="Обратно",
            page=self.page,
            bg=ApplicationSettings().bg_color,
            color=ApplicationSettings().color
        ).get_filled_tonal_btn()
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
        check_box_for_password_field: Checkbox = CheckBoxReg(
            text="Показать пароль",
            page=self.page,
            field=password_field
        ).get_check_box()
        text_error = TextError(txt="").get_text_error()
        self.view_registration.controls = [
            btn_gnr,
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
                        check_box_for_password_field,
                        flet_app.Row(
                            controls=[
                                OutlineButton(
                                    text="Зарегистрироваться",
                                    width=ApplicationSettings().width_outl_btn,
                                    color=ApplicationSettings().bd_color_outl,
                                    to_page="Процесс регистрации",
                                    page_now=self.page,
                                    field_email=email_field,
                                    field_password=password_field,
                                    error=text_error
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
                    top=125
                )
            )
        ]

    def view(self, page: flet_app.Page, params: Params, basket: Basket):

        #Установка компонентов
        self.set_components()

        return self.view_registration