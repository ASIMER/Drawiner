import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
class Settings(Widget):
	"""This class planned to visualize settings as widget
	which contains buttons and key-binding"""
	keys = {"Move": {
				"move_up": "w",
				"move_down": "s",
				"move_left": "a",
				"move_right": "d"
				},
			"Combat": {
				"fire": "space"
				},
			"Additional": {
				"Move": {
					"move_up": "up",
					"move_down": "down",
					"move_left": "left",
					"move_right": "right"
					}
				},
				"Combat": {
					"fire": ""
					},
			}
	def __init__(self):
		super(Settings, self).__init__()