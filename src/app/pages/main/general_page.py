#Other libraries
import flet
from flet import (
    Page,
    View,
    Container,
    BorderRadius,
    Image,
    Row,
    Column,
    Text,
    MainAxisAlignment,
    CrossAxisAlignment,
    margin,
    FontWeight,
    TextAlign,
    colors,
    ExpansionTile,
    ListView,
    ListTile,
    FilledTonalButton,
    LinearGradient,
    Alignment,
    Border,
    Icon,
    DataTable,
    DataCell,
    DataRow,
    DataColumn
)
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.settings.application_settings import ApplicationSettings
from src.session import UserSession
from src.db.services.user_service import UserService
from src.app.pages.page_fabric import PageFabric
from src.app.components.button.filled_tonal_button_reg import FilledTonalButtonReg
from src.db.services.history_service import HistoryService


class GeneralPage(PageFabric):

    def __init__(self):
        self.view_general: View = View(route="/general")

    def set_components(self) -> None:
        #Получение данных
        user_data: dict = UserService().get_one(id_user=UserSession.id_user)

        btn_update_username: FilledTonalButton = FilledTonalButtonReg(
            text="Обновить имя",
            page=self.page,
            bg=colors.INDIGO_ACCENT_200,
            color="BLACK"
        ).get_filled_tonal_btn()

        btn_update_password: FilledTonalButton = FilledTonalButtonReg(
            text="Обновить пароль",
            page=self.page,
            bg=colors.GREEN_ACCENT_200,
            color="BLACK"
        ).get_filled_tonal_btn()

        btn_update_userphoto: FilledTonalButton = FilledTonalButtonReg(
            text="Обновить фотографию",
            page=self.page,
            bg=colors.RED_ACCENT,
            color="BLACK"
        ).get_filled_tonal_btn()

        self.view_general.controls = [
            Row(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Container(
                                    content=Text(
                                        value="Меню",
                                        weight=FontWeight.BOLD,
                                        size=22,
                                        italic=True
                                    ),
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
                                    content=MenuBarApplication(page=self.page, is_selected=0).get_menu(),
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
                    Container(
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Column(
                                            controls=[
                                                Image(
                                                    src="/home/darkfos/PycharmProjects/finance_app/src/static/images/base_profile.png",
                                                    width=90,
                                                    height=90
                                                ),
                                            ],
                                        ),
                                        Column(
                                            controls=[
                                                Text(value=user_data.get("username")),
                                                Text(value=user_data.get("email")),
                                            ]
                                        ),
                                        Container(

                                        )
                                    ],
                                    spacing=30
                                ),
                                Row(
                                    controls=[
                                        Text(value=""),
                                        Text(value="")
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Column(
                                            controls=[
                                                Container(
                                                    content=Text(
                                                        value="Моя статистика",
                                                        weight=FontWeight.W_500,
                                                        size=16,
                                                        text_align=TextAlign.CENTER
                                                    ),

                                                    width=160,
                                                    height=25,
                                                    bgcolor=colors.INDIGO_ACCENT_200,
                                                    border_radius=BorderRadius(
                                                        top_right=12,
                                                        top_left=12,
                                                        bottom_right=12,
                                                        bottom_left=12
                                                    )
                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Конвертация валют: "
                                                        ),
                                                        Text(
                                                            value=user_data.get('count_convert_coin'),
                                                            color='ORANGE'
                                                        )
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Конвертация коинов: "
                                                        ),
                                                        Text(
                                                            value=user_data.get("count_general_convert"),
                                                            color="ORANGE"
                                                        )
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Всего: ",
                                                            weight=FontWeight.W_500,
                                                            italic=True
                                                        ),
                                                        Text(
                                                            value=user_data.get("count_general_convert"),
                                                            color="ORANGE"
                                                        ),
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Дата регистрации: ",
                                                            weight=FontWeight.W_500,
                                                            italic=True
                                                        ),
                                                        Text(
                                                            value=user_data.get("data_registration"),
                                                            color=colors.GREEN_ACCENT_200
                                                        )
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Дата обновления: ",
                                                            weight=FontWeight.W_500,
                                                            italic=True
                                                        ),
                                                        Text(
                                                            value=user_data.get("data_update"),
                                                            color=colors.GREEN_ACCENT_200
                                                        ),
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(""),
                                        Text(""),
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Container(
                                            content=Text(
                                                value="Другое",
                                                size=16,
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.CENTER
                                            ),
                                            width=160,
                                            height=25,
                                            bgcolor=colors.RED_ACCENT_200,
                                            border_radius=BorderRadius(
                                                top_right=12,
                                                top_left=12,
                                                bottom_right=12,
                                                bottom_left=12
                                            )
                                        )
                                    ]
                                ),
                                ListView(
                                    controls=[
                                        ExpansionTile(
                                            leading=Icon(flet.icons.HISTORY),
                                            title=Text(value="История"),
                                            subtitle=Text(value="Ваша история"),
                                            text_color="blue",
                                            expand=True,
                                            controls=[
                                                DataTable(
                                                    columns=[
                                                        DataColumn(
                                                            Text(
                                                                value="Операция №1",
                                                                color=colors.GREEN_ACCENT_200
                                                            )
                                                        ),
                                                        DataColumn(
                                                            Text(
                                                                value="Операция №2",
                                                                color=colors.GREEN_ACCENT_200
                                                            )
                                                        ),
                                                        DataColumn(
                                                            Text(
                                                                value="Дата операции",
                                                                color=colors.ORANGE_ACCENT_200
                                                            )
                                                        )
                                                    ],
                                                    rows=[
                                                        DataRow(
                                                            cells=[
                                                                DataCell(
                                                                    Text(value=history.get("from_operation"))
                                                                ),
                                                                DataCell(
                                                                    Text(value=history.get("to_operation"))
                                                                ),
                                                                DataCell(
                                                                    Text(value=history.get("date_operation"))
                                                                ),
                                                            ]
                                                        )
                                                        for history in HistoryService().get_all(id_user=UserSession.id_user)
                                                    ]
                                                )
                                            ]
                                        ),
                                        ExpansionTile(
                                            leading=Icon(flet.icons.SAVE),
                                            title=Text(value="Безопасность"),
                                            subtitle=Text(value="Настройки безопасности"),
                                            text_color="blue",
                                            expand=True,
                                            controls=[
                                                Column(
                                                    controls=[
                                                        Text(value=""),
                                                        Row(
                                                            controls=[
                                                                Text(value="Обновление имени: "),
                                                                btn_update_username
                                                            ]
                                                        ),
                                                        Row(
                                                            controls=[
                                                                Text(value="Обновление пароля: "),
                                                                btn_update_password
                                                            ]
                                                        ),
                                                        Row(
                                                            controls=[
                                                                Text(value="Обновление фотографии: "),
                                                                btn_update_userphoto
                                                            ]
                                                        ),
                                                    ],
                                                    spacing=25,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                    alignment=MainAxisAlignment.CENTER
                                                )
                                            ],
                                        ),
                                    ],
                                    height=ApplicationSettings().height_application - 450,
                                    width=500,
                                    animate_rotation=True,
                                )
                            ]
                        ),
                        width=ApplicationSettings().weight_application - ApplicationSettings().weight_application // 4,
                        height=ApplicationSettings().height_application - 50,
                        margin=margin.only(left=60, top=0, right=0, bottom=0)
                    ),
                ]
            )
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_general