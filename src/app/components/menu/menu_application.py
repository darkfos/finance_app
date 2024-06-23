from flet import NavigationRail, NavigationRailDestination, icons, colors
from src.settings.application_settings import ApplicationSettings


class MenuBarApplication:

    def __init__(self):
        self.navigation: NavigationRail = NavigationRail(
            width=ApplicationSettings().weight_application // 4,
            height=ApplicationSettings().height_application,
            bgcolor=colors.INDIGO_ACCENT_200,
            destinations=[
                NavigationRailDestination(
                    icon=icons.START,
                    label="Главная страница",
                    padding=2,
                    indicator_color="black"
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
                    indicator_color="black"
                ),
                NavigationRailDestination(
                    icon=icons.SETTINGS,
                    label="Настройки",
                    indicator_color="black"
                )
            ]
        )

    def get_menu(self) -> NavigationRail:
        return self.navigation