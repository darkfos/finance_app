#System
from typing import Union, Dict, List


#Other
from requests import Session


#Local
from src.settings.auth_settings import AuthSettings


class CoinValue:

    def __init__(self):
        self.session = Session()
        self.auth: AuthSettings = AuthSettings()

    def get_currencies(self) -> Union[Dict[Union[str, int], Union[str, int, float, None]], None]:
        """
        Получение электронных валют
        :return:
        """

        response = self.session.get(
            url=self.auth.url_course_coin+"currencies",
            params={
                "api_key": self.auth.api_coin_value_key
            }
        )

        if response.status_code == 200:
            return response.json()

        return None

    def get_currencies_symbols(self) -> Union[Dict[str, List[Dict[str, int]]], None]:
        """
        Получение всех криптовалют и их цеников
        :return:
        """

        response = self.get_currencies()

        if response:
            all_currencies: dict = {}
            for value in response.get("data"):
                all_currencies[value.get("name")] = {
                    "price": value.get("values").get("USD").get("price"),
                    "symbol": value.get("symbol")
                }
            return all_currencies
        return None

    def convert_crypt_to_usd(self, value: Union[int, float], crypt_name: str) -> Union[None, float]:
        """
        Конвертация криптовалюты в доллары
        :return:
        """

        currencies = self.get_currencies_symbols()

        if currencies:
            if crypt_name in currencies:
                return currencies.get(crypt_name).get("price") * value
        return None