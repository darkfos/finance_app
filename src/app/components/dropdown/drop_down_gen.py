#System
from typing import List


#Other
from flet import Dropdown, Page, ControlEvent
import flet


#Local
from src.settings.application_settings import ApplicationSettings


class DropDownGeneral:

    def __init__(self, list_objects: List[str], label: str = ""):
        self.dr_menu: Dropdown = Dropdown(
            label=label,
            options=[flet.dropdown.Option(data=obj_data, key=obj_data) for obj_data in list_objects],
            autofocus=True,
            on_change=self.change_elements,
            width=ApplicationSettings().dr_down_weight
        )

    def change_elements(self, e):
        data = e.control


    def get_drop_down_menu(self) -> Dropdown:
        return self.dr_menu