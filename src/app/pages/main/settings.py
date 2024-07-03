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
    Text,
    FontWeight
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
                                    border_radius=BorderRadius(top_right=48, bottom_right=0, top_left=0, bottom_left=0)
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
                                    border_radius=BorderRadius(top_right=0, bottom_right=48, top_left=0, bottom_left=0)
                                ),
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