from Ship import Ship
from AbstractObjects import Singleton


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
    # inventory = Inventory()
    source = 'img/usership.png'