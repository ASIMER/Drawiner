from abc import ABCMeta, abstractmethod


class IDataSerializer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def serialize_data(data):
        pass


class IDataSaver(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def save_data(data):
        pass


class IDataLoader(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def load_data(data):
        pass
