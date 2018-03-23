import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.vector import Vector
class Ship(Image):
	hp = 0
	mp = 0
	xp = 0
	ammo = 0
	boost = (0, "type")
	heat = {
		#(heat value, overheat(planned), thruster down timer(planned))
		"forward_t": [0, 0, 0],
		"backward_t": [0, 0, 0],
		"left_t": [0, 0, 0],
		"right_t": [0, 0, 0], 
		"weapon_1": [0, 0, 0]
		}
	#inventory = Inventory()
	source = 'img/usership.png'
	coords = ObjectProperty(Vector(0, 0), True)
	velocity = ObjectProperty(Vector(0, 0), True)
	def flight_assist(self):
		#if must check value higher then norm vect multiply value, to prevent loop
		if (self.velocity.length() > 0.06):
			self.velocity = (self.velocity 
							+ self.velocity.normalize().rotate(180) 
							* 0.05)
		else:
			self.velocity = Vector(0, 0)
	def overheat(self, heat_type):
		self.heat[heat_type][0] += 0.006
		if(self.heat[heat_type][0] >= 1):
			self.heat[heat_type][0] = 1
	def thrust(self, direction):
		if (direction == "forward_t"):
			self.velocity = (self.velocity 
							+ Vector(0.1, 0).rotate(self.angle) 
							* self.heat[direction][0])
			self.overheat(direction)
		elif (direction == "backward_t"):
			self.velocity = (self.velocity
							+ Vector(0.05, 0).rotate(self.angle+180) 
							* self.heat[direction][0])
			self.overheat(direction)
		elif (direction == "left_t"):
			self.velocity = (self.velocity
							+ Vector(0.03, 0).rotate(self.angle+90)
							* self.heat[direction][0])
			self.overheat(direction)
		elif (direction == "right_t"):
			self.velocity = (self.velocity
							+ Vector(0.03, 0).rotate(self.angle+270)
							* self.heat[direction][0])
			self.overheat(direction)
	def move(self):
		self.coords = self.coords + self.velocity
		for htype in self.heat:
			if (self.heat[htype][0] > 0):
				self.heat[htype][0] -= 0.004
			else:
				self.heat[htype][0] = 0