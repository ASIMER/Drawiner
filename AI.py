from Ship import Ship
from kivy.vector import Vector
from abc import ABCMeta, abstractmethod


class AI(Ship):
    mass = 1000000
    cooldown = {
        "Bullet": 0,
    }
    selected_ammo = "Bullet"
    weapon = "Cannon"
    heat = {
        # (heat value, overheat(planned), thruster down timer(planned))
        "forward_t": [0, 0, 0],
        "backward_t": [0, 0, 0],
        "left_t": [0, 0, 0],
        "right_t": [0, 0, 0],
        "weapon_1": [0, 0, 0]
    }


    def __init__(self, user, *args, **kwargs):
        self.user = user
        self.source = 'img/usership.png'
        super().__init__(*args, **kwargs)
    def thrust(self, direction):

        if self.velocity.length() > self.max_speed:
            self.velocity = self.velocity.normalize()*self.max_speed
            return

        if direction == "forward_t":
            self.velocity = (self.velocity
                             + Vector(0.1, 0).rotate(self.angle)
                             * self.heat[direction][0])
            self.overheat(direction)
        elif direction == "backward_t":
            self.velocity = (self.velocity
                             + Vector(0.05, 0).rotate(self.angle + 180)
                             * self.heat[direction][0])
            self.overheat(direction)
        elif direction == "left_t":
            self.velocity = (self.velocity
                             + Vector(0.03, 0).rotate(self.angle + 90)
                             * self.heat[direction][0])
            self.overheat(direction)
        elif direction == "right_t":
            self.velocity = (self.velocity
                             + Vector(0.03, 0).rotate(self.angle + 270)
                             * self.heat[direction][0])
            self.overheat(direction)