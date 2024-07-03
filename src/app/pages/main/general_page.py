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
    ListTile
)
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.settings.application_settings import ApplicationSettings
from src.session import UserSession
from src.db.services.user_service import UserService
from src.app.pages.page_fabric import PageFabric


class GeneralPage(PageFabric):

    def __init__(self):
        self.view_general: View = View(route="/general")

    def set_components(self) -> None:
        #Получение данных
        user_data: dict = UserService().get_one(id_user=UserSession.id_user)

        self.view_general.controls = [
            Row(
                controls=[
                    Container(
                        content=MenuBarApplication(page=self.page, is_selected=0).get_menu(),
                        border_radius=BorderRadius(top_right=48, bottom_right=48, top_left=0, bottom_left=0)
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
                                            title=Text(value="История"),
                                            subtitle=Text(value="Ваша история"),
                                            expand=True,
                                            controls=[ListTile(title=Text(value="Test"))]
                                        ),
                                        ExpansionTile(
                                            title=Text(value="Безопасность"),
                                            subtitle=Text(value="Настройки безопасности"),
                                            expand=True,
                                            controls=[ListTile(title=Text(value="Тест"))]
                                        ),
                                    ],
                                    height=ApplicationSettings().height_application - 400,
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