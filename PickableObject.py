from AbstractObjects import MovableObject
from Settings import Settings
from CustomExceptions import NoSuchPickableObjectTypeException


class PickableObject(MovableObject):

    def __init__(self, potype='PlushTrap', **kwargs):
        self.potype = potype
        super().__init__(**kwargs)

    def collide(self, object_picker):
        if self.potype == 'HPBonus':
            object_picker.hp += Settings.bonuses['HPBonus']
        elif self.potype == 'SpeedBonus':
            object_picker.speed += Settings.bonuses['SpeedBonus']
        elif self.potype == 'AmmoBonus':
            object_picker.ammo += Settings.bonuses['AmmoBonus']
        elif self.potype == 'DamageTrap':
            object_picker.hp -= Settings.bonuses['DamageTrap']
        elif self.potype == 'SpeedTrap':
            object_picker.speed -= Settings.bonuses['SpeedTrap']
        elif self.potype == 'PlushTrap':
            pass  # screamer
        else:
            raise NoSuchPickableObjectTypeException(self.potype, "No such type of bonus/trap exists")
        del self
