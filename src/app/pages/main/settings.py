from flet import Page, View
from flet_route import Params, Basket
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class SettingsPage(PageFabric):

    def __init__(self):
        self.view_settings: View = View(route="/settings")

    def set_components(self):
        self.view_settings.controls = [
            MenuBarApplication(page=self.page, is_selected=4).get_menu()
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:
        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_settings