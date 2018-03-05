import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from Keyboard import *
from Mouse import *
from Canvas import *
from Menu import *
from Interface import *
from Settings import *
from Asteroid import *
from Ai import *

class DrawinerApp(App):
	angle = 0
	def build(self):
		self.game = Game()
		self.keyboard = Keyboard()
		self.mouse = Mouse()
		self.settings = Settings()
		Clock.schedule_interval(self.update, 1.0/60.0)
		return self.game
	def update(self, dt):
		self.game.ship.angle = (Vector(Window.mouse_pos)-Vector(Window.width/2, Window.height/2)).angle(Vector(1,0))
		print(self.game.ship.angle)
		if (len(self.keyboard.key_set)!=0): print(self.keyboard.key_set)
		for key in self.keyboard.key_set:
			if (key in self.settings.keys["Move"]["move_up"]):
				print("move_up test")
				self.game.ship.coord_y += 1
			elif (key in self.settings.keys["Move"]["move_down"]):
				print("move_down test")
				self.game.ship.coord_y -= 1
			elif (key in self.settings.keys["Move"]["move_left"]):
				print("move_left test")
				self.game.ship.coord_x -= 1
			elif (key in self.settings.keys["Move"]["move_right"]):
				print("move_right test")
				self.game.ship.coord_x += 1
			elif (key in self.settings.keys["Combat"]["fire"]):
				print(Window.width)
				print(self.game.coords_label.text)
				print(self.game.ship.coords)
		if (len(self.keyboard.del_key_set) != 0):
			print(self.keyboard.del_key_set)
			self.keyboard.key_set -= self.keyboard.del_key_set
			self.keyboard.del_key_set.clear()
DrawinerApp().run()