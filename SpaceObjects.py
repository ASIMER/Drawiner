from AbstractObjects import MovableObject
from GameDataModule import GameData


class BlackHole(MovableObject):

    def __init__(self, speed_gravity, *args, **kwargs):
        self.speed_gravity = speed_gravity
        super().__init__(*args, **kwargs)

    def gravitate(self):
        obj_list = GameData.get_objects_list()
        for obj in obj_list:
            direction_vector = self.coords - obj.coords
            obj.velocity += self.speed_gravity*direction_vector.normalize()/pow(direction_vector.length(), 2)
