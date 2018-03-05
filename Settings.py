import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
class Settings(Widget):
	"""This class planned to visualize settings as widget
	which contains buttons and key-binding"""
	keys = {"Move": {
				"move_up": ("w", "up"),
				"move_down": ("s", "down"),
				"move_left": ("a", "left"),
				"move_right": ("d", "right")
				},
			"Combat": {
				"fire": "spacebar"
				}
			}
	def __init__(self):
		super(Settings, self).__init__()