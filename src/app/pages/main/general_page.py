import flet
from flet import Page, View, Column, Container, MainAxisAlignment, BorderRadius
from flet_route import Params, Basket
from src.settings.application_settings import ApplicationSettings
from src.app.components.menu.menu_application import MenuBarApplication


class GeneralPage:

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        view_general_page: View = View("/general")
        view_general_page.controls = [
            Container(
                content=MenuBarApplication(page=page, is_selected=0).get_menu(),
                border_radius=BorderRadius(top_right=48, bottom_right=48, top_left=0, bottom_left=0)
            ),
            Container()
        ]

        return view_general_page