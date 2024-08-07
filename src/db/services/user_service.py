#System
from typing import Union, Dict, List


#Other libraries
from bson.objectid import ObjectId
from pydantic import EmailStr


#Local
from src.db.abs_mongo import MongoABC
from src.db.engine import MongoEngine
from src.db.dto.user_dto import AddNewUser


class UserService(MongoEngine, MongoABC):
    def get_one(self, id_user: ObjectId) -> Union[Dict, None]:
        """
        Получение пользователя по id
        :param id_user:
        :return:
        """

        user = self.user_collection.find_one({"_id": id_user})
        if user:
            return user
        return None

    def get_all(self) -> List[AddNewUser]:
        """
        Получение всех пользователей
        :return:
        """

        return self.user_collection.find()

    def add_new(self, new_user: AddNewUser) -> bool:
        """
        Добавление нового пользователя
        :param new_user:
        :return:
        """

        is_created = self.user_collection.insert_one(new_user.model_dump())
        return True if is_created else False

    def delete_one(self, id_user: ObjectId) -> bool:
        """
        Удаление пользователя
        :return:
        """

        is_deleted = self.user_collection.delete_one({"id": id_user})
        if is_deleted:
            return True
        return False

    def update_information(self, find_data: dict, data_update: dict) -> bool:
        """
        Обновление информации
        :return:
        """

        is_updated = self.user_collection.update_one(find_data, data_update)
        if is_updated: return True
        return False

    def find_user_by_email(self, email: EmailStr, password: str) -> bool:
        """
        Поиск пользователей по email и password
        :param email:
        :return:
        """

        user: dict = self.user_collection.find_one({"email": email})
        if user:
            if user.get("password") == password:
                return True
            else:
                return False
        else:
            return False

    def find_user_auth(self, email: str) -> Union[Dict, bool]:
        """
        Поиск пользователя по email
        :param email:
        :return:
        """

        user: dict = self.user_collection.find_one({"email": email})
        if user: return user
        return False