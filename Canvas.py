import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
class Game(Widget):
	"""
	main_sky = None
	skybox_1 = ObjectProperty(None)
	skybox_2 = ObjectProperty(None)
	skybox_3 = ObjectProperty(None)
	skybox_4 = ObjectProperty(None)
	"""
	ship = ObjectProperty(None)
	def build(self):
		self.ship.bind(on_coords = self.move)
	def move(self):
		pass
		#if (((self.skybox_1.center_x - self.skybox.size/2) <= center_x <= ) and ):

		#elif():
		#print(self.skybox_4.pos)
		#print(self.skybox_4.size)