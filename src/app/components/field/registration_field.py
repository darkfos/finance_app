from flet import TextField


def registration_field(text: str, width: int) -> TextField:
    """
    Создание текстового поля
    :param text:
    :return:
    """

    text_field: TextField = TextField(
        label=text,
        width=width
    )

    return text_field