from flet import TextField


class RegistrationField:

    def __init__(self, text: str, width: int):
        self.field = TextField(label=text, width=width)

    def get_field(self) -> TextField:
        return self.field