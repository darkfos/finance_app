from flet import View, Page
from flet_route import Params, Basket
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class Directory(PageFabric):

    def __init__(self):
        self.view_directory: View = View(route="/directory")

    def set_components(self):
        self.view_directory.controls = [
            MenuBarApplication(page=self.page, is_selected=3).get_menu()
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:
        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_directory