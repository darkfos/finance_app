from flet import Text, TextStyle, FontWeight


class TextError:

    def __init__(self, txt: str):
        self.text = Text(value=txt, style=TextStyle(
            color="red",
            weight=FontWeight.W_500
        ))

    def get_text_error(self) -> Text:
        return self.text