import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from Ship import *
class Game(Widget):
	skybox_1 = ObjectProperty(None)
	skybox_2 = ObjectProperty(None)
	skybox_3 = ObjectProperty(None)
	skybox_4 = ObjectProperty(None)
	ship = ObjectProperty(None)
	skybox_pos_x = NumericProperty(0)
	skybox_pos_y = NumericProperty(0)
	skybox_pos = ReferenceListProperty(skybox_pos_x, skybox_pos_y)
	print(ship)

	def move(self):
		return