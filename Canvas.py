import kivy
kivy.require("1.10.0")
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.core.window import Window
from kivy.vector import Vector
class Game(Widget):
	main_sky = None
	skybox_1 = ObjectProperty(None)
	skybox_2 = ObjectProperty(None)
	skybox_3 = ObjectProperty(None)
	skybox_4 = ObjectProperty(None)
	ship = ObjectProperty(None)
	def build(self):
		self.ship.bind(on_coords = self.move)
	def get_main_sky(self, finded, *args):
		for img in args:
			if ((img.pos[0] <= finded.center_x <= img.pos[0] + img.size[0]) and 
			(img.pos[1] <= finded.center_y <= img.pos[1] + img.size[1])):
				return img
		return -1
	def get_quarter(self, source, finded):
		if ((source.center_x <= finded.center_x) and 
			(source.center_y <= finded.center_y)):
			return 1
		elif ((source.center_x > finded.center_x) and 
			(source.center_y <= finded.center_y)):
			return 2
		elif ((source.center_x > finded.center_x) and 
			(source.center_y > finded.center_y)):
			return 3
		elif ((source.center_x <= finded.center_x) and 
			(source.center_y > finded.center_y)):
			return 4
		else:
			return 1
	def move(self):
		main_sky = self.get_main_sky(self.ship, self.skybox_1, 
									self.skybox_2, self.skybox_3, 
									self.skybox_4)
		quarter = self.get_quarter(main_sky, self.ship)
		"""
		if quarter == 1:
			for i in [skybox_1, skybox_2, skybox_3, skybox_4]:
				if i == main_sky:
					break
				else:

		elif quarter == 2:
		"""

		#elif():
		#print(self.skybox_4.pos)
		#print(self.skybox_4.size)