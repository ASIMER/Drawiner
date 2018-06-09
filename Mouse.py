from kivy.core.window import Window
from Manipulator import Manipulator


class Mouse(Manipulator):
    key_set = set()
    del_key_set = set()

    def __init__(self, **kwargs):
        super(Mouse, self).__init__(**kwargs)
    def bind(self):
        Window.bind(on_touch_down=self.key_down)
        Window.bind(on_touch_up=self.key_up)

    def key_down(self, touched_object, touch):
        self.key_set.add("mouse " + touch.button)

    def key_up(self, touched_object, touch):
        self.del_key_set.add("mouse " + touch.button)
    def close(self):
        pass