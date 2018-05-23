from abc import ABCMeta, abstractmethod


class ISaver(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def save_data(data):
        pass


class ILoader(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def load_data():
        pass


class ISerializer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def serialize_data(data):
        pass
