from AbstractObjects import DestructableObject
from Engines import GeometryEngine

class Asteroid(DestructableObject):
    def __init__(self, user, parent, *args, **kwargs):
        self.user = user
        self.logic_parent = parent

        self.source = 'img/asteroid2.png'
        super().__init__(*args, **kwargs)
    '''def check_distance(self):
        if GeometryEngine.dist_square(self.user.coords, self.coords) < 40000 and not self in self.logic_parent.children:
                self.logic_parent.add_widget(self)
                print("lol")
        elif GeometryEngine.dist_square(self.user.coords, self.coords) > 40000 and self in self.logic_parent.children:
            self.logic_parent.remove_widget(self)
            self.coords = self.user.coords
            self.logic_parent.add_widget(self)
            print("kek")'''