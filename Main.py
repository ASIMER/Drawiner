import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from Keyboard import *
from Canvas import *
from Menu import *
from Interface import *
from Settings import *
from Asteroid import *
from Ai import *

class DrawinerApp(App):
	def build(self):
		self.game = Game()
		self.keyboard = Keyboard()
		Clock.schedule_interval(self.update, 1.0/60.0)
		return self.game
	def update(self, dt):
		self.keyboard.key_set.clear()
DrawinerApp().run()