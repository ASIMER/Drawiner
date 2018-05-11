from AbstractObjects import DestructableObject


class Ship(DestructableObject):

    def __init__(self, ammo=200, *args, **kwargs):
        self.ammo = ammo
        super().__init__(*args, **kwargs)

    def shoot(self):
        pass # Bullet()