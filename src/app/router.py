#Other libraries
import flet as flet_app
from flet_route import Routing, path


#Pages
from src.app.pages.auth.application_auth import AuthenticationPage
from src.app.pages.auth.applicatin_registration import RegistrationPage
from src.app.pages.main.general_page import GeneralPage
from src.app.pages.main.course_value import CourseValue
from src.app.pages.main.course_crypt import CourseCrypt
from src.app.pages.main.directory import Directory
from src.app.pages.main.settings import SettingsPage
from src.settings.application_settings import ApplicationSettings


class Router:

    def __init__(self, page: flet_app.Page):
        self.page = page
        self.flet_app = flet_app

        #Установка настроек
        self.page.window_width = ApplicationSettings.weight_application
        self.page.window_height = ApplicationSettings.height_application
        self.page.window_resizable = ApplicationSettings.resizable_window
        self.page.title = ApplicationSettings.title_application

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
                view=GeneralPage().view
            ),
            path(
                url="/course_value",
                clear=True,
                view=CourseValue().view
            ),
            path(
                url="/course_crypt",
                clear=True,
                view=CourseCrypt().view
            ),
            path(
                url="/directory",
                clear=True,
                view=Directory().view
            ),
            path(
                url="/settings",
                clear=True,
                view=SettingsPage().view
            )
        ]

        Routing(page=self.page, app_routes=app_routers)
        self.page.go("/")