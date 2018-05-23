class ClassGetter:

    @staticmethod
    def get_class(class_name):
        class_object = globals()[class_name]
        return class_object

    @staticmethod
    def get_class_name(instance):
        return instance.__class__.__name__
