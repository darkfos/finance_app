#Other libraries
from flet import (
    Page,
    View,
    LinearGradient,
    Alignment,
    Row,
    BorderRadius,
    Container,
    Column,
    MainAxisAlignment,
    CrossAxisAlignment,
)
import flet
from flet_route import Params, Basket


#Local
from src.settings.application_settings import ApplicationSettings
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class SettingsPage(PageFabric):

    def __init__(self):
        self.view_settings: View = View(route="/settings")

    def set_components(self):
        self.view_settings.controls = [
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
                                    content=MenuBarApplication(page=self.page, is_selected=4).get_menu(),
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
                ]
            )
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:
        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_settings