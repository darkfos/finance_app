#Other libraries
from flet import Page, IconButton, colors, icons


class IconButtonForLeave:

    def __init__(self, page: Page):
        self.page = page
        self.icon_btn: IconButton = IconButton(
            icon=icons.EXIT_TO_APP,
            icon_color="RED",
            on_click=self.on_click_icon_btn
        )

    def on_click_icon_btn(self, e):
        """
        Выход из приложения, очистка памяти
        :param e:
        :return:
        """

        with open("user_data.txt", "w") as file:
            file.write("")

        self.page.go("/")

    def get_icon_btn(self) -> IconButton:
        return self.icon_btn