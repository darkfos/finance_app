from flet import TextField


class RegistrationField:

    def __init__(self, text: str, width: int, password: bool = False):
        self.field = TextField(label=text, width=width, password=password)

    def get_field(self) -> TextField:
        return self.field