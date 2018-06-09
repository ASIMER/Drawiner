from kivy.core.window import Window
from FactoryManipulator import FactoryManipulator
from Keyboard import Keyboard
from Mouse import Mouse


class CreateKeyboard(FactoryManipulator):
    def set_type(self):
        self.type = Keyboard()
        self.key_set = self.type.key_set
        self.del_key_set = self.type.del_key_set

class CreateMouse(FactoryManipulator):
    def set_type(self):
        self.type = Mouse()
        self.key_set = self.type.key_set
        self.del_key_set = self.type.del_key_set