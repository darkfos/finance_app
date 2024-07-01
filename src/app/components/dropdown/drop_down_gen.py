#System
from typing import List, Union


#Other
from flet import Dropdown, Page, ControlEvent, icons
import flet


#Local
from src.settings.application_settings import ApplicationSettings


class DropDownGeneral:

    def __init__(self, list_objects: List[str], label: str = "", width: Union[float, None] = None, icon: icons = None):
        self.dr_menu: Dropdown = Dropdown(
            label=label,
            options=[flet.dropdown.Option(data=obj_data, key=obj_data) for obj_data in list_objects],
            autofocus=True,
            on_change=self.change_elements,
            width=ApplicationSettings().dr_down_weight if not width else width,
            icon=icon if icon else ...
        )

    def change_elements(self, e):
        data = e.control


    def get_drop_down_menu(self) -> Dropdown:
        return self.dr_menu