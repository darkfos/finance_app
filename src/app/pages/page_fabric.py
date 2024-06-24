from abc import ABC, abstractmethod


class PageFabric(ABC):

    @abstractmethod
    def set_components(self):
        pass

    @abstractmethod
    def view(self, *args):
        pass