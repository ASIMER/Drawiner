import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
class Settings(Widget):
	"""docstring for Settings"""
	def __init__(self, arg):
		super(Settings, self).__init__()
		self.arg = arg
