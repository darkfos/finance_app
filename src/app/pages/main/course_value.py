#Other libraries
from flet import (
    Column,
    Text,
    View,
    Page,
    Row,
    Container,
    BorderRadius,
    Dropdown,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextField,
    Border,
    LinearGradient,
    Alignment
)
from flet_route import Params, Basket
import flet


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.settings.application_settings import ApplicationSettings
from src.app.components.button.reg_button import OutlineButton
from src.app.components.dropdown.drop_down_gen import DropDownGeneral
from src.app.components.field.registration_field import RegistrationField
from src.app.pages.page_fabric import PageFabric


class CourseValue(PageFabric):
    def __init__(self):
        self.view_course_value: View = View(route="/course_value")

    def set_components(self):
        drop_down_menu: Dropdown = DropDownGeneral(list_objects=[
            "AUD",
            "USD",
            "RUB",
            "EUR",
            "AMD",
            "CNY",
            "JPY",
            "NOK",
            "SEK",
            "UAH",
            "PLN"
        ]).get_drop_down_menu()
        drop_down_menu_2: Dropdown = DropDownGeneral(list_objects=[
            "AUD",
            "USD",
            "RUB",
            "EUR",
            "AMD",
            "CNY",
            "JPY",
            "NOK",
            "SEK",
            "UAH",
            "PLN"
        ]).get_drop_down_menu()
        field_values_1: TextField = RegistrationField(
            text="Валюта №1",
            width=ApplicationSettings().weight_application-250
        ).get_field()

        field_values_2: TextField = RegistrationField(
            text="Итог конвертации",
            width=ApplicationSettings().weight_application-250,
            disable_field=True
        ).get_field()
        text_result: Text = Text(value="")

        self.view_course_value.controls = [
            Row(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Container(
                                    border=flet.border.only(right=flet.border.BorderSide(1, "0xff870160")),
                                    alignment=flet.alignment.center,
                                    gradient=LinearGradient(
                                        begin=flet.alignment.top_left,
                                        end=Alignment(0.8, 1),
                                        colors=[
                                            "0xff1f005c",
                                            "0xff5b0060",
                                            "0xff870160",
                                            "0xffac255e",
                                            "0xffca485c",
                                            "0xffe16b5c",
                                            "0xfff39060",
                                            "0xffffb56b",
                                        ],
                                        tile_mode=flet.GradientTileMode.MIRROR,
                                        rotation=3.14 / 2
                                    ),
                                    width=ApplicationSettings().weight_application // 4,
                                    height=90,
                                    border_radius=BorderRadius(top_right=48, bottom_right=0, top_left=0, bottom_left=0)
                                ),
                                Container(
                                    content=MenuBarApplication(page=self.page, is_selected=1).get_menu(),
                                    border=flet.border.only(right=flet.border.BorderSide(1, "0xff870160")),
                                    alignment=flet.alignment.center,
                                    gradient=LinearGradient(
                                        begin=flet.alignment.top_left,
                                        end=Alignment(0.8, 1),
                                        colors=[
                                            "0xff1f005c",
                                            "0xff5b0060",
                                            "0xff870160",
                                            "0xffac255e",
                                            "0xffca485c",
                                            "0xffe16b5c",
                                            "0xfff39060",
                                            "0xffffb56b",
                                        ],
                                        tile_mode=flet.GradientTileMode.MIRROR,
                                        rotation=3.14 / 2
                                    ),
                                    width=ApplicationSettings().weight_application // 4,
                                    # height=ApplicationSettings().weight_application,
                                    border_radius=BorderRadius(top_right=0, bottom_right=48, top_left=0, bottom_left=0)
                                )
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        )
                    ),
                    Column(
                        controls=[
                            field_values_1,
                            field_values_2,
                            Row(
                                controls=[
                                    drop_down_menu,
                                    OutlineButton(
                                        text="Конвертировать",
                                        width=ApplicationSettings().width_outl_btn - 50,
                                        to_page="Конвертация валют",
                                        page_now=self.page,
                                        color=ApplicationSettings().bd_color_outl,
                                        dr_1=drop_down_menu,
                                        dr_2=drop_down_menu_2,
                                        field_1=field_values_1,
                                        field_2=field_values_2,
                                        error=text_result
                                    ).get_btn(),
                                    drop_down_menu_2
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER,
                                spacing=40
                            ),
                            text_result
                        ],
                        spacing=30,
                        width=ApplicationSettings().weight_application-250,
                        height=ApplicationSettings().height_application - 250,
                    ),
                ]
            )
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        #Set components
        self.page = page
        self.set_components()

        return self.view_course_value