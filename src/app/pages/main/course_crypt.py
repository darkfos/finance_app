#Other libraries
from flet import (
    Page,
    View,
    Row,
    Column,
    Container,
    icons,
    TextField,
    Dropdown,
    OutlinedButton,
    MainAxisAlignment,
    BorderRadius,
    CrossAxisAlignment,
    Text,
    LinearGradient,
    Border,
    Alignment
)
import flet
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.components.dropdown.drop_down_gen import DropDownGeneral
from src.settings.application_settings import ApplicationSettings
from src.app.components.field.registration_field import RegistrationField
from src.app.components.button.reg_button import OutlineButton
from src.api.crypt.coin_value import CoinValue
from src.app.pages.page_fabric import PageFabric


class CourseCrypt(PageFabric):

    def __init__(self):
        self.view_course_crypt: View = View(route="/course_crypt")
        self.coin_value: CoinValue = CoinValue()

    def set_components(self):

        amount: TextField = RegistrationField(
            text="Количество",
            width=ApplicationSettings().field_width + 100,
            password=False,
            icon=icons.PRODUCTION_QUANTITY_LIMITS
        ).get_field()

        amount_result: TextField = RegistrationField(
            text="Итог",
            width=ApplicationSettings().field_width + 100,
            password=False,
            icon=icons.PRODUCTION_QUANTITY_LIMITS,
            disable_field=True
        ).get_field()

        #Получаем все криптовалюты
        all_crypto = self.coin_value.get_currencies_symbols()

        drop_down: Dropdown = DropDownGeneral(
            label="Криптовалюта",
            list_objects=[crypt_data for crypt_data in all_crypto.keys()],
            width=ApplicationSettings().field_width + 100,
            icon=icons.CURRENCY_BITCOIN
        ).get_drop_down_menu()

        error_text: Text = Text(value="")

        btn_convert: OutlinedButton = OutlineButton(
            text="Конвертировать",
            width=ApplicationSettings().width_outl_btn,
            color=ApplicationSettings().bd_color_outl,
            dr_1=drop_down,
            field_1=amount,
            field_2=amount_result,
            to_page="Конвертация криптовалюты",
            page_now=self.page,
            error=error_text
        ).get_btn()

        self.view_course_crypt.controls = [
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
                                    content=MenuBarApplication(page=self.page, is_selected=2).get_menu(),
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
                            amount,
                            amount_result,
                            drop_down,
                            btn_convert,
                            error_text
                        ],
                        width=ApplicationSettings().weight_application - ApplicationSettings().weight_application // 4,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=15,
                        alignment=MainAxisAlignment.CENTER,
                    )
                ]
            )
        ]

    def view(self, page: Page, params: Params, basket: Basket):

        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_course_crypt