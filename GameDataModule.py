from DBProcessor import DBSaver, DBLoader


class ClassGetter:

    @staticmethod
    def get_class(class_name):
        class_object = globals()[class_name]
        return class_object

    @staticmethod
    def get_class_name(instance):
        return instance.__class__.__name__


class GameData:

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
        GameData.__objects_list.remove(obj)

    @staticmethod
    def serialize_data():
        return Serializer.serialize(GameData.__objects_list)

    @staticmethod
    def save_data():
        DBSaver.save(GameData.serialize_data())

    @staticmethod
    def load_data():
        GameData.__objects_list = DBLoader.load()


class Serializer:

    # serializes and returns only the attributes those are inherited in an object's instance
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
    def serialize(objects_list):
        data_list = []
        for instance in objects_list:
            instance_data = [ClassGetter.get_class_name(instance), Serializer.serialize_attr_dict(instance.__dict__)]
            # serialized attributes' dict is [attr_list, types_list, values_list] list
            data_list.append(instance_data)

        return data_list
