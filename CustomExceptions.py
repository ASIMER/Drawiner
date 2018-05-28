from ClassGetter import ClassGetter
from Settings import Settings


class NoSuchObjectInGameError(ValueError):

    @staticmethod
    def print_object_data(obj):
        print(obj + "data")
        print(ClassGetter.get_class_name(obj))
        for attr, value in obj.__dict__:
            print(attr + ":" + value)
        print()

    def __init__(self, objects_list, specified_object, *args, **kwargs):
        print("Specified object " + specified_object + " was not found")
        print("List of the objects in game:")
        print()
        print(map(NoSuchObjectInGameError.print_object_data, objects_list))
        print()
        print("End of the list")
        super().__init__(*args, **kwargs)


class NoSuchPickableObjectTypeException(Exception):

    @staticmethod
    def print_possible_types():
        for potype in Settings.bonuses:
            print(potype)

    def __init__(self, specified_type):
        print("Specified type " + specified_type + " was not found")
        print("List of the possible types:")
        print()
        NoSuchPickableObjectTypeException.print_possible_types()
        print()
        print("End of the list")