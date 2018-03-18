import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
class Settings(Widget):
	"""This class planned to visualize settings as widget
	which contains buttons and key-binding"""
	FA = False
	keys = {
		"Move": {
			"move_up": ("w", "up"),
			"move_down": ("s", "down"),
			"move_left": ("a", "left"),
			"move_right": ("d", "right")
			},
		"Combat": {
			"fire": "spacebar"
			},
		"Utils": {
			"FA": ["z", False]
			}
		}
	#PLANNED FEATURES	
	difficulty = {
		"Normal": {
			"Overheat": {
				"forward_t": 0,
				"backward_t": 0,
				"left_t": 0,
				"right_t": 0,
				"weapon_t": 0,
				}
			}
		}
	def __init__(self):
		super(Settings, self).__init__()