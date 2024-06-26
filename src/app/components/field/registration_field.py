from flet import TextField


class RegistrationField:

    def __init__(self, text: str, width: int, password: bool = False, disable_field: bool = False):
        self.field = TextField(label=text, width=width, password=password, disabled=disable_field)

    def get_field(self) -> TextField:
        return self.field