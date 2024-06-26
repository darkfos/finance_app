#System
from typing import List

#Other
from flet import Dropdown, Page, ControlEvent
import flet


class DropDownGeneral:

    def __init__(self, list_objects: List[str], label: str = ""):
        self.dr_menu: Dropdown = Dropdown(
            label=label,
            options=[flet.dropdown.Option(data=obj_data, key=obj_data) for obj_data in list_objects],
            autofocus=True,
            on_change=self.change_elements
        )

    def change_elements(self, e):
        data = e.control
        print(data.value)

    def get_drop_down_menu(self) -> Dropdown:
        return self.dr_menu