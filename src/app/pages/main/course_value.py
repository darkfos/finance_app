#Other libraries
from flet import Column, Text, View, Page, Row, Container, BorderRadius, Dropdown
from flet_route import Params, Basket
import flet


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.app.components.dropdown.drop_down_gen import DropDownGeneral
from src.app.pages.page_fabric import PageFabric


class CourseValue(PageFabric):
    def __init__(self):
        self.view_course_value: View = View(route="/course_value")

    def set_components(self):
        drop_down_menu: Dropdown = DropDownGeneral(list_objects=["Рубль", "Евро", "Рупий", "Доллар"]).get_drop_down_menu()

        self.view_course_value.controls = [
            Row(
                controls=[
                    Container(
                        content=MenuBarApplication(is_selected=1, page=self.page).get_menu(),
                        border_radius=BorderRadius(top_right=48, bottom_right=48, top_left=0, bottom_left=0)
                    ),
                    Column(
                        controls=[
                            drop_down_menu
                        ],
                    ),
                ]
            )
        ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        #Set components
        self.page = page
        self.set_components()

        return self.view_course_value