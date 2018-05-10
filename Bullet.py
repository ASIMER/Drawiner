import kivy
kivy.require("1.10.0")
from MovableObject import MovableObject
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from Settings import Settings
class Bullet(MovableObject):
	hp = 0
	def __init__(self, type, shooter):
		self.shooter = shooter
		self.angle =  self.shooter.angle
		super().__init__()
		if type in Settings.Ammo:
			self.source = Settings.Ammo[type]["image"]
			self.coords = self.coords + shooter.coords
			self.velocity = (shooter.velocity + self.velocity + Vector(1, 0).rotate(shooter.angle) * Settings.Weapons[shooter.weapon]["fire power"] / Settings.Ammo[type]["mass"])
		else:
			raise NameError("Bullet type doesn't exist")