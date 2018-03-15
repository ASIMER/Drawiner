import kivy
kivy.require("1.10.0")
from kivy.core.window import Window
from kivy.uix.widget import Widget
class Mouse(Widget):
	"""Keyboard module for listening keyboard inputs, by DCP©"""
	def __init__(self, **kwargs):
		super(Mouse, self).__init__(**kwargs)
		Window.bind(on_cursor_enter = self.on_touch_move_test)
		"""Мой юный дцпшник, импут_тайп нужен что бы на яблофоне выбрать нужную клаву"""
	def on_touch_move_test (self, touch_obj):
		return