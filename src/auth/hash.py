import hashlib
from src.settings.auth_settings import AuthSettings


class HashService:

    def __init__(self):
        self.__salt: str = AuthSettings.salt

    def hash_password(self, password: str) -> str:
        """
        Хэширование пароля
        :param password:
        :return:

        WHERE
        n - коэффицент стоимости процессора, памяти
        r - размер блока,
        p - коэффицент распараллеливания
        """

        hash_password = hashlib.scrypt(password=password.encode(), salt=self.__salt.encode(), n=8, r=512, p=4, dklen=32)

        return hash_password.hex()

    def verify(self, password_found: str, user_password: str) -> bool:
        """
        Проверка паролей
        :param password_found:
        :param user_password:
        :return:
        """

        h_ps = self.hash_password(password=user_password)

        return True if h_ps == password_found else False