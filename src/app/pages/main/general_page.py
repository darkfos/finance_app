import flet
from flet import Page, View, Column, Container, MainAxisAlignment, BorderRadius
from flet_route import Params, Basket
from src.settings.application_settings import ApplicationSettings
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class GeneralPage(PageFabric):

    def __init__(self):
        self.view_general: View = View(route="/general")

    def set_components(self) -> None:

        self.view_general.controls = [
            Container(
                content=MenuBarApplication(page=self.page, is_selected=0).get_menu(),
                border_radius=BorderRadius(top_right=48, bottom_right=48, top_left=0, bottom_left=0)
            ),
            Container()
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_general