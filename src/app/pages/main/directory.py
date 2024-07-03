#Other libraries
import flet
from flet import (
    View,
    ListView,
    Page,
    ExpansionTile,
    Row,
    Column,
    Text,
    Container,
    BorderRadius,
    FontWeight,
    MainAxisAlignment,
    ScrollMode,
    TileAffinity,
    Icon,
    icons,
    Alignment,
    LinearGradient,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    colors,
    CrossAxisAlignment
)
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.settings.application_settings import ApplicationSettings
from src.app.pages.page_fabric import PageFabric


class Directory(PageFabric):

    def __init__(self):
        self.view_directory: View = View(route="/directory")

    def set_components(self):
        self.view_directory.controls = [
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
                                        border=flet.border.only(right=flet.border.BorderSide(1, "#2573da")),
                                        alignment=flet.alignment.center,
                                        gradient=LinearGradient(
                                            begin=flet.alignment.top_left,
                                            end=Alignment(5, 1),
                                            colors=[
                                                "#3225da",
                                                "#2573da",
                                                "#25cdda",
                                                "#25cdda",
                                                "#2573da",
                                            ],
                                            tile_mode=flet.GradientTileMode.CLAMP,
                                            rotation=0.1
                                        ),
                                        width=ApplicationSettings().weight_application // 4,
                                        height=90,
                                        border_radius=BorderRadius(top_right=48, bottom_right=0, top_left=0,
                                                                   bottom_left=0)
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                MenuBarApplication(page=self.page, is_selected=0).get_menu(),
                                                Text(""),
                                                flet.IconButton(
                                                    icon=flet.icons.EXIT_TO_APP,
                                                    icon_color="RED",
                                                    on_click=lambda _: self.page.go("/"),
                                                ),
                                                Text(""),
                                                Text("")
                                            ],
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                        ),
                                        border=flet.border.only(right=flet.border.BorderSide(1, "#2573da")),
                                        border_radius=BorderRadius(top_right=0, bottom_right=48, top_left=0,
                                                                   bottom_left=0)
                                    ),
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            )
                        ),
                        ListView(
                            width=ApplicationSettings().weight_application - 270,
                            height=ApplicationSettings().height_application - 50,
                            controls=[
                                Container(
                                    content=Column(
                                        controls=[
                                            Text(value="Краткая информация", weight=FontWeight.W_700, size=24),
                                            ExpansionTile(
                                                leading=Icon(name=icons.QUESTION_MARK),
                                                title=Text(value="Что это за приложение"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[
                                                    flet.ListTile(
                                                        title=Text(value="Finance - это приложение, которое поможет " +
                                                                         "пользователю узнать курс валют, курс электронных валют, просматривать личную статистику"))
                                                ],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.DESCRIPTION),
                                                title=Text(value="Энциклопедия"),
                                                subtitle=Text(value="Finance"),
                                                expanded_cross_axis_alignment=CrossAxisAlignment.START,
                                                maintain_state=True,
                                                controls=[
                                                    Text(
                                                        value="\nНиже приведён список из валют, которые имеются на данный" + \
                                                        " момент времени в приложении\n",
                                                        weight=FontWeight.W_500
                                                    ),
                                                    DataTable(
                                                        columns=[
                                                            DataColumn(Text(
                                                                value="Валюта",
                                                                color=colors.GREEN_ACCENT_200
                                                            )),
                                                            DataColumn(Text(
                                                                value="Описание",
                                                                color=colors.GREEN_ACCENT_200
                                                            ))
                                                        ],
                                                        rows=[
                                                            DataRow(
                                                                cells=[
                                                                    DataCell(Text(value=coin_data[0])),
                                                                    DataCell(Text(value=coin_data[-1]))
                                                                ]
                                                            )
                                                            for coin_data in ApplicationSettings().coin_value_data.items()
                                                        ]
                                                    ),
                                                    Text(
                                                        value="\nСписок имеющихся криптовалют в данном приложении\n",
                                                        weight=FontWeight.W_500
                                                    ),
                                                    DataTable(
                                                        columns=[
                                                            DataColumn(
                                                                Text(
                                                                    value="Валюта",
                                                                    color=colors.ORANGE_ACCENT_200
                                                                )
                                                            ),
                                                            DataColumn(
                                                                Text(
                                                                    value="Описание криптовалюты",
                                                                    color=colors.ORANGE_ACCENT_200
                                                                )
                                                            )
                                                        ],
                                                        rows=[
                                                            DataRow(
                                                                cells=[
                                                                    DataCell(
                                                                        Text(value=data_coin[0])
                                                                    ),
                                                                    DataCell(
                                                                        Text(value=data_coin[-1])
                                                                    )
                                                                ]
                                                            )
                                                            for data_coin in ApplicationSettings.crypt_coin_value_data.items()
                                                        ]
                                                    ),
                                                ],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.INFO),
                                                title=Text(value="Возможности приложения"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[flet.ListTile(title=Text(value="Их нет"))],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.DEVELOPER_BOARD),
                                                title=Text(value="Создатель"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[
                                                    flet.ListTile(title=Text(value="darkfos\nTelegram: @Silmarion"))],
                                                text_color="blue",
                                            ),
                                        ],
                                    ),
                                )
                            ]
                        )
                    ]
                )
            ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:
        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_directory