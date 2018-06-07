from GameDataModule import GameData
from Engines import GeometryEngine as ge
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.properties import ObjectProperty


class MovableObject(Image):

    coords = ObjectProperty(Vector(0, 0), True)
    velocity = ObjectProperty(Vector(0, 0), True)

    def __init__(self, instance=None, mass=1000, max_speed=10, boost=1, max_boost=100, *args, **kwargs):
        self.max_speed = max_speed
        self.boost = boost
        self.max_boost = max_boost
        self.size = (100, 100)
        super().__init__(*args, **kwargs)
        GameData.add_obj(self)

    def move(self):
        self.coords = self.coords + self.velocity

    def check_collision(self):
        objects_list = GameData.get_objects_list()
        for obj in objects_list:
            if obj == self:
                continue
            if ge.are_circles_intersected(self.coords, self.size, obj.coords, obj.size):
                self.collide(obj)

    def collide(self, obj):
        # self.get_damage(obj.collide_damage). Instances of the class cannot get damage
        obj.get_damage(self.collide_damage)

    def get_damage(self, damage):
        pass

    def __del__(self):
        GameData.rem_obj(self)


class DestructableObject(MovableObject):

    def __init__(self, collide_damage=20, hp=100, *args, **kwargs):
        self.collide_damage = collide_damage
        self.hp = hp
        super().__init__(self, *args, **kwargs)

    def collide(self, obj):
        self.get_damage(obj.collide_damage)
        obj.get_damage(self.collide_damage)

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            del self


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls.instance
        else:
            return cls.instance
