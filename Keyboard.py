import kivy
kivy.require("1.10.0")
from kivy.core.window import Window
from kivy.uix.widget import Widget
class Keyboard(Widget):
	"""Keyboard module for listening keyboard inputs, by DCP©"""
	key_set = set()
	del_key_set = set()
	def __init__(self, **kwargs):
		super(Keyboard, self).__init__(**kwargs)
		"""Мой юный дцпшник, импут_тайп нужен что бы на яблофоне выбрать нужную клаву"""
		self._keyboard = Window.request_keyboard(self.close_keyboard, self, input_type='text')
		self._keyboard.bind(on_key_down = self.input)
		self._keyboard.bind(on_key_up = self.key_up)
		#Window.bind(on_keyboard = self.input)
	def input(self, keyboard_obj, key, text, modifier):
		self.key_set.add(key[1])
	def key_up(self, keyboard_obj, key):
		self.del_key_set.add(key[1])
	def close_keyboard(self):
		Window.unbind(on_keyboard = self.get_key)
		del self._keyboard