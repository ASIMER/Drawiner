class Settings:
    """This class planned to visualize settings as widget
    which contains buttons and key-binding"""
    FA = False
    keys = {
        "Move": {
            "move_up": ("w", "up"),
            "move_down": ("s", "down"),
            "move_left": ("a", "left"),
            "move_right": ("d", "right")
        },
        "Combat": {
            "fire": ("spacebar", "mouse left")
        },
        "Utils": {
            "FA": ["z", False]
        },
    }
    # PLANNED FEATURES
    difficulty = {
        "Normal": {
            "Overheat": {
                "forward_t": 0,
                "backward_t": 0,
                "left_t": 0,
                "right_t": 0,
                "weapon_t": 0,
            }
        }
    }
    Weapons = {
        "Cannon": {
            "image": None,
            "mass": 100,
            "AI": None,
            "fire power": 200000
        }
    }
    Ammo = {
        "Bullet": {
            "image": "img/bullet.png",
            "mass": 10000,
            "AI": None
        }
    }
    bonuses = {
        'HPBonus': 50,
        'SpeedBonus': 5,
        'AmmoBonus': 100,
        'HPTrap': 50,
        'SpeedTrap': 5
    }