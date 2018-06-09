from kivy.core.window import Window
from Manipulator import Manipulator

class Keyboard(Manipulator):
    key_set = set()
    del_key_set = set()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bind(self):
        self._keyboard = Window.request_keyboard(self.close,
                                                 self, input_type='text'
                                                 )
        self._keyboard.bind(on_key_down=self.key_down)
        self._keyboard.bind(on_key_up=self.key_up)

    def key_down(self, keyboard_obj, key, text, modifier):
        self.key_set.add(key[1])

    def key_up(self, keyboard_obj, key):
        self.del_key_set.add(key[1])

    def close(self):
        Window.unbind(on_keyboard=self.get_key)
        del self._keyboard
