from abc import ABC, abstractmethod


class MongoABC(ABC):

    @abstractmethod
    def get_one(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_all(self, *args, **kwargs):
        pass

    @abstractmethod
    def add_new(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_one(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_information(self, *args, **kwargs):
        pass