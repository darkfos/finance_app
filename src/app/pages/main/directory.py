#Other libraries
import flet
from flet import (
    View,
    ListView,
    Page,
    ExpansionTile,
    Row,
    Column,
    Text,
    Container,
    BorderRadius,
    FontWeight,
    MainAxisAlignment,
    ScrollMode,
    TileAffinity,
    Icon,
    icons
)
from flet_route import Params, Basket


#Local
from src.app.components.menu.menu_application import MenuBarApplication
from src.settings.application_settings import ApplicationSettings
from src.app.pages.page_fabric import PageFabric


class Directory(PageFabric):

    def __init__(self):
        self.view_directory: View = View(route="/directory")

    def set_components(self):
        self.view_directory.controls = [
                Row(
                    controls=[
                        Container(
                            MenuBarApplication(page=self.page, is_selected=3).get_menu(),
                            border_radius=BorderRadius(top_right=48, bottom_right=48, top_left=0, bottom_left=0)
                        ),
                        ListView(
                            width=ApplicationSettings().weight_application - 270,
                            height=ApplicationSettings().height_application - 50,
                            controls=[
                                Container(
                                    content=Column(
                                        controls=[
                                            Text(value="Краткая информация", weight=FontWeight.W_700, size=24),
                                            ExpansionTile(
                                                leading=Icon(name=icons.QUESTION_MARK),
                                                title=Text(value="Что это за приложение"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[
                                                    flet.ListTile(
                                                        title=Text(value="Finance - это приложение, которое поможет " +
                                                                         "пользователю узнать курс валют, курс электронных валют, просматривать личную статистику"))
                                                ],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.DESCRIPTION),
                                                title=Text(value="Энциклопедия"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[flet.ListTile(
                                                    title=Text(
                                                        value="USD - United States Dollar, курс доллара (Американский).\n\n" + \
                                                              "AUD - Australian Dollar, курс доллара (Австралийского)\n\n" + \
                                                              "RUB - Russian Ruble, курс русского рубля\n\n" + \
                                                              "EUR - Euro, курс евро\n\n" + \
                                                              "AMD - Armenian Dram, курс армянского драма\n\n" + \
                                                              "CNY - <b>Chinese Yuan</b>, курс китайского юаня\n\n" + \
                                                              "JPY - Japanese Yen, курс японского йена\n\n" + \
                                                              "NOK - Norwegian Krone, курс норвежского крона\n\n" + \
                                                              "SEK - Swedish Krona, курс шведского крона\n\n" + \
                                                              "UAH - Ukrainian Hryvnia, курс украинской гривны\n\n" + \
                                                              "PLN - Polish Zloty, курс польской злоты"
                                                    )
                                                )
                                                ],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.INFO),
                                                title=Text(value="Возможности приложения"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[flet.ListTile(title=Text(value="Их нет"))],
                                                text_color="blue"
                                            ),
                                            ExpansionTile(
                                                leading=Icon(name=icons.DEVELOPER_BOARD),
                                                title=Text(value="Создатель"),
                                                subtitle=Text(value="Finance"),
                                                maintain_state=True,
                                                controls=[
                                                    flet.ListTile(title=Text(value="darkfos\nTelegram: @Silmarion"))],
                                                text_color="blue",
                                            ),
                                        ],
                                    ),
                                )
                            ]
                        )
                    ]
                )
            ]

    def view(self, page: Page, params: Params, basket: Basket) -> View:
        #Установка компонентов
        self.page = page
        self.set_components()

        return self.view_directory