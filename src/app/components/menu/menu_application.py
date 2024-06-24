from typing import Union
from flet import (
    NavigationRail,
    NavigationRailDestination,
    icons,
    colors,
    OptionalEventCallback,
    Page,
    View
)
from src.settings.application_settings import ApplicationSettings


class MenuBarApplication:

    def __init__(self, page: Page, is_selected: Union[int, None] = None):
        self.page: Page = page
        self.navigation: NavigationRail = NavigationRail(
            width=ApplicationSettings().weight_application // 4,
            height=ApplicationSettings().height_application,
            bgcolor=colors.INDIGO_ACCENT_200,
            destinations=[
                NavigationRailDestination(
                    icon=icons.HOUSE,
                    label="Профиль",
                    padding=2,
                    indicator_color="black",
                ),
                NavigationRailDestination(
                    icon=icons.MONEY,
                    label="Курсы валют",
                    padding=2,
                    indicator_color="black"
                ),
                NavigationRailDestination(
                    icon=icons.CURRENCY_BITCOIN,
                    label="Курсы коинов",
                    padding=2,
                    indicator_color="black"
                ),
                NavigationRailDestination(
                    icon=icons.INFO,
                    label="Краткая информация",
                    padding=2,
                    indicator_color="black",
                ),
                NavigationRailDestination(
                    icon=icons.SETTINGS,
                    label="Настройки",
                    indicator_color="black"
                )
            ],
            on_change=self.change_body_application
        )

        if is_selected:
            self.navigation.selected_index = is_selected

    def change_body_application(self, e: OptionalEventCallback):
        """
        Изменение body приложения
        :param e:
        :return:
        """

        match e.control.selected_index:
            case 0:
                self.page.go("/general")
            case 1:
                self.page.go("/course_value")
            case 2:
                self.page.go("/course_crypt")
            case 3:
                self.page.go("/directory")
            case 4:
                self.page.go("/settings")
            case _:
                ...

    def get_menu(self) -> NavigationRail:
        return self.navigation