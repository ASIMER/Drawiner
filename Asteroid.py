from AbstractObjects import DestructableObject
from Engines import GeometryEngine

class Asteroid(DestructableObject):
    def __init__(self, user, parent, *args, **kwargs):
        self.user = user
        self.logic_parent = parent

        self.source = 'img/asteroid2.png'
        super().__init__(*args, **kwargs)