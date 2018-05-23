from DBProcessor import DBSaver, DBLoader, DBSerializer
from CustomExceptions import NoSuchObjectInGameError
from DataProcessingInterfaces import IDataSerializer, IDataSaver, IDataLoader


class ClassGetter:

    @staticmethod
    def get_class(class_name):
        class_object = globals()[class_name]
        return class_object

    @staticmethod
    def get_class_name(instance):
        return instance.__class__.__name__


class GameData(IDataSerializer, IDataSaver, IDataLoader):

    __objects_list = []

    @staticmethod
    def get_objects_list():
        return GameData.__objects_list

    @staticmethod
    def add_obj(obj):
        GameData.__objects_list.append(obj)

    @staticmethod
    def rem_obj(obj):
        return None
        if obj in GameData.__objects_list:
            GameData.__objects_list.remove(obj)
        else:
            raise NoSuchObjectInGameException(GameData.get_objects_list(), obj, "No such object exists in game")

    @staticmethod
    def serialize_data():
        return Serializer.serialize_data(GameData.__objects_list)

    @staticmethod
    def save_data():
        DBSaver.save_data()

    @staticmethod
    def load_data():
        GameData.__objects_list = DBSerializer.deserialize_data(DBLoader.load_data())


class Serializer(IDataSerializer):

    # serializes and returns only the attributes those an object's instance does not have
    @staticmethod
    def serialize_attr_dict(attr_dict):
        obj_instance = object()
        attr_list = []
        types_list = []
        values_list = []
        for key, value in attr_dict:
            if not hasattr(obj_instance, key):
                attr_list.append(key)
                types_list.append(ClassGetter.get_class_name(value))
                values_list.append(value)

        return [attr_list, types_list, values_list]

    @staticmethod
    def serialize_data(objects_list):
        data_list = []
        for instance in objects_list:
            instance_data = [ClassGetter.get_class_name(instance), Serializer.serialize_attr_dict(instance.__dict__)]
            # serialized attributes' dict is [attr_list, types_list, values_list] list
            data_list.append(instance_data)

        return data_list
