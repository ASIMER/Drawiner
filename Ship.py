from kivy.app import App
from kivy.vector import Vector
from Settings import Settings
from AbstractObjects import DestructableObject
from Bullet import Bullet


class Ship(DestructableObject):

    def __init__(self, ammo=200, *args, **kwargs):
        self.ammo = ammo
        super().__init__(*args, **kwargs)

    def cooling(self, speed):
        for cooldown_type in self.cooldown:
            if self.cooldown[cooldown_type] > 0:
                self.cooldown[cooldown_type] = round(self.cooldown[cooldown_type] - 0.1, 1)

    def flight_assist(self):
        # if must check value higher then norm vect multiply value, to prevent loop
        if self.velocity.length() > 0.06:
            self.velocity = (self.velocity
                             + self.velocity.normalize().rotate(180)
                             * 0.05)
        else:
            self.velocity = Vector(0, 0)

    def overheat(self, heat_type):
        self.heat[heat_type][0] += 0.006
        if self.heat[heat_type][0] >= 1:
            self.heat[heat_type][0] = 1

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

    def move(self):
        self.coords = self.coords + self.velocity
        for htype in self.heat:
            if self.heat[htype][0] > 0:
                self.heat[htype][0] -= 0.004
            else:
                self.heat[htype][0] = 0

    def fire(self):
        if self.cooldown[self.selected_ammo] == 0:
            bullet = Bullet(self.selected_ammo, self)
            self.thrust("backward_t")
            self.velocity = self.velocity - Vector(1, 0).rotate(self.angle) * Settings.Weapons[self.weapon][
                "fire power"] / self.mass
            App.get_running_app().bullets += [bullet]
            self.parent.add_widget(bullet)
            self.cooldown["Bullet"] = 1