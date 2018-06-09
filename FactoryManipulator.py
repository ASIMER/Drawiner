from kivy.core.window import Window
from Manipulator import Manipulator


class FactoryManipulator(Manipulator):
    type = None
    def __init__(self):
        return self.type.__init__()
    def binding(self):
        return self.type.bind()
    def key_down(self):
        return self.type.key_down()

    def key_up(self):
        return self.type.key_up()

    def close(self):
        return self.type.close_keyboard()

    def set_type(self):
        raise AttributeError("Не задан тип устройства ввода!")