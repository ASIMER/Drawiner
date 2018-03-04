import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
class Ship(Image):
	hp = 0
	mp = 0
	xp = 0
	ammo = 0
	#inventory = Inventory()
	source = 'img/usership.png'
	coord_x = NumericProperty(0)
	coord_y = NumericProperty(0)
	coords = ReferenceListProperty(coord_x, coord_y)
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	def move(self):
		self.coords = self.coords + Vector(*self.velocity)