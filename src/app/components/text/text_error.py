from flet import Text, TextStyle, FontWeight
from src.settings.application_settings import ApplicationSettings


class TextError:

    def __init__(self, txt: str):
        self.text = Text(value=txt, style=TextStyle(
            color=ApplicationSettings().error_color,
            weight=FontWeight.W_500
        ))

    def get_text_error(self) -> Text:
        return self.text