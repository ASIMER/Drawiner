from AbstractObjects import DestructableObject
from kivy.vector import Vector
from Settings import Settings


class Bullet(DestructableObject):
    def __init__(self, bultype, shooter, *args, **kwargs):
        self.shooter = shooter
        self.angle = self.shooter.angle
        super().__init__(*args, **kwargs)
        if bultype in Settings.Ammo:
            self.source = Settings.Ammo[bultype]["image"]
            self.coords = self.coords + shooter.coords
            self.velocity = (
                shooter.velocity + self.velocity + Vector(1, 0).rotate(shooter.angle) *
                Settings.Weapons[shooter.weapon][
                    "fire power"] / Settings.Ammo[bultype]["mass"])
        else:
            raise NameError("Bullet type doesn't exist")
