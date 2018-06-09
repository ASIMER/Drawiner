from abc import ABCMeta, abstractmethod
from kivy.uix.widget import Widget

class Manipulator(Widget):
    __metaclass__ = ABCMeta
    key_set = set()
    del_key_set = set()
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def key_down(self):
        pass
    @abstractmethod
    def key_up(self):
        pass
    @abstractmethod
    def close(self):
        pass