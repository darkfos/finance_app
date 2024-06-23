import flet
from flet import Page, View, Column, Container, MainAxisAlignment, BorderRadius
from flet_route import Params, Basket
from src.settings.application_settings import ApplicationSettings
from src.app.components.menu.menu_application import MenuBarApplication


class GenerapPage:

    def view(self, page: Page, params: Params, basket: Basket) -> View:

        return View(
            "/general",
            controls=[
                MenuBarApplication().get_menu(),
                Column()
            ]
        )