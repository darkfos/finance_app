from flet import Page, View
from flet_route import Params, Basket
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class CourseCrypt(PageFabric):

    def __init__(self):
        self.view_course_crypt: View = View(route="/course_crypt")

    def set_components(self):
        self.view_course_crypt.controls = [
            MenuBarApplication(page=self.page, is_selected=2).get_menu()
        ]

    def view(self, page: Page, params: Params, basket: Basket):

        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_course_crypt