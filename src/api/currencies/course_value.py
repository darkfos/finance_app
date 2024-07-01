#Other
from requests import Session
from typing import Dict, Union


#Local
from src.settings.auth_settings import AuthSettings


class CourseValue:

    def __init__(self):
        self.session: Session = Session()
        self.auth: AuthSettings = AuthSettings()

    def get_all_values(self) -> Union[Dict[str, int], None]:
        """
        Получение всех имеющихся валют
        :return:
        """

        response = self.session.get(
            url=self.auth.url_course_value+"/latest",
            params={
                "access_key": self.auth.api_course_value_key
            }
        )

        if response.status_code == 200:
            response = response.json()
            return {value: response.get("rates").get(value) for value in response.get("rates")}

        return None

    def get_information_about_values(self) -> Union[Dict[str, Union[str, int]], None]:
        """
        Получение информации о валютах
        :return:
        """

        response = self.session.get(
            url=self.auth.url_course_value+"/symbols",
            params={
                "access_key": self.auth.api_course_value_key
            }
        )

        if response.status_code == 200:
            return response.json().get("symbols")
        return None

    def convert_value(self, value_1: str, value_2: str, amount: int) -> Union[int, None]:
        """
        Конвертация 1 валюты в другую
        :param value_1:
        :param value_2:
        :param amount:
        :return:
        """

        all_data_currencies: Dict[str, int] = self.get_all_values()

        if all_data_currencies:
            initial_value = amount / all_data_currencies.get(value_1)
            return round(initial_value * all_data_currencies.get(value_2), 2)

        return None