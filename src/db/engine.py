from typing import List, Dict, Union

from pymongo import MongoClient
from bson.objectid import ObjectId
from src.settings.db_settings import DatabaseSettings
from src.db.abs_mongo import MongoABC
from src.db.dto.user_dto import AddNewUser, UpdateUserInformation


class MongoEngine(MongoABC):
    def __init__(self):
        self.engine: MongoClient = MongoClient(DatabaseSettings.db_url)
        self.db = self.engine["finance"]
        self.user_collection = self.db["users"]

    def get_one(self, id_user: ObjectId) -> Union[Dict, None]:
        """
        Получение пользователя по id
        :param id_user:
        :return:
        """

        user = self.user_collection.find_one({"id": id_user})
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

    def update_information(self, data_update: UpdateUserInformation) -> bool:
        """
        Обновление информации
        :return:
        """

        is_updated = self.user_collection.update_one(data_update.model_dump())
        if is_updated: return True
        return False