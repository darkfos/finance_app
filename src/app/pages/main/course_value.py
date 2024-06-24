#Other libraries
from flet import Container, Text, View, Page
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.pages.page_fabric import PageFabric


class CourseValue(PageFabric):
    def __init__(self):
        self.view_course_value: View = View(route="/course_value")

    def set_components(self):
        self.view_course_value.controls = [
            MenuBarApplication(is_selected=1, page=self.page).get_menu()
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        #Set components
        self.page = page
        self.set_components()

        return self.view_course_value