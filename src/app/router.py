import flet as flet_app
from flet_route import Routing, path


#Pages
from src.app.pages.auth.application_auth import AuthenticationPage
from src.app.pages.auth.applicatin_registration import RegistrationPage
from src.app.pages.main.general_page import GenerapPage


class Router:

    def __init__(self, page: flet_app.Page):
        self.page = page
        self.flet_app = flet_app

        self.start_router()

    def start_router(self):

        app_routers: list[path] = [
            path(
                url="/",
                clear=True,
                view=AuthenticationPage().view
            ),
            path(
                url="/registration",
                clear=True,
                view=RegistrationPage().view
            ),
            path(
                url="/general",
                clear=True,
                view=GenerapPage().view
            )
        ]

        Routing(page=self.page, app_routes=app_routers)
        self.page.go("/")