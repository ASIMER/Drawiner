from Ship import Ship
from AbstractObjects import Singleton
from kivy.vector import Vector


class UserShip(Ship, Singleton):
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

    source = 'img/usership.png'

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