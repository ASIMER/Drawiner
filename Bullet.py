import kivy
kivy.require("1.10.0")
from MovableObject import MovableObject
from kivy.vector import Vector
from kivy.properties import ObjectProperty
class Bullet(MovableObject):
	hp = 0
	def __init__(self, type, shooter):
		self.shooter = shooter
		self.angle =  self.shooter.angle
		super().__init__()
		if type == "bullet":
			self.source = 'img/bullet.png'
			self.coords = self.coords + shooter.coords
			self.velocity = (self.velocity + Vector(20, 0).rotate(shooter.angle))