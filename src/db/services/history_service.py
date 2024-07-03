#System
from typing import Union, Dict, List


#Other libraries
from bson.objectid import ObjectId


#Local
from src.db.abs_mongo import MongoABC
from src.db.engine import MongoEngine
from src.db.dto.history_dto import AddHistory


class HistoryService(MongoABC, MongoEngine):

    def get_one(self, id_user: ObjectId) -> Union[bool, Dict]:
        """
        Поиск истории по id пользователя
        :param _id_history:
        :return:
        """

        user_history = self.user_history_collection.find_one({"user_id": id_user})
        if user_history: return user_history
        else:
            return False

    def get_all(self, id_user) -> Union[List, List[Dict]]:
        """
        Получение всей истории пользователя по id
        :param args:
        :param kwargs:
        :return:
        """

        all_history_user: List[Dict] = self.user_history_collection.find(
            {"user_id": id_user}
        )
        return all_history_user

    def add_new(self, new_history: AddHistory) -> bool:
        """
        Добавление новое истории
        :new_history:
        :return:
        """

        is_created: bool = self.user_history_collection.insert_one(new_history.model_dump())
        if is_created: return True
        return False

    def delete_one(self, id_history: ObjectId):
        """
        Удаление истории
        :param args:
        :param kwargs:
        :return:
        """

        is_deleted: bool = self.user_history_collection.delete_one({"_id": id_history})
        return True if is_deleted else False

    def update_information(self, *args, **kwargs):
        """
        Обновление истории
        :param args:
        :param kwargs:
        :return:
        """

        pass