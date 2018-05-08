from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.vector import Vector
class MovableObject(Image):
	coords = ObjectProperty(Vector(0, 0), True)
	velocity = ObjectProperty(Vector(0, 0), True)
	def move(self):
		self.coords = self.coords + self.velocity