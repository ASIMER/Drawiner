import kivy

kivy.require("1.10.0")
from kivy.app import App
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from Keyboard import Keyboard
from Mouse import Mouse
from Canvas import Game
from Settings import Settings
from Asteroid import Asteroid
from AI import AI
from random import randint
from functools import partial
from Creators import CreateKeyboard, CreateMouse
from pprint import pprint


class DrawinerApp(App):
    bullets = []
    asteroids = []
    bots = []

    def build(self):
        self.game = Game()
        self.keyboard = CreateKeyboard()
        self.keyboard.set_type()
        self.keyboard.binding()
        self.mouse = CreateMouse()
        self.mouse.set_type()
        self.mouse.binding()
        self.settings = Settings()
        # Create loop with 1/60 sec delay
        for i in range(0, 200):
            self.asteroids.append(Asteroid(parent=self.game, user=self.game.usership,
                                           coords=Vector(randint(-5000, 5000), randint(-5000, 5000))))
            self.game.add_widget(self.asteroids[i])
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        AI1 = AI(user=self.game.usership)
        self.bots.append(AI1)
        self.game.add_widget(AI1)
        return self.game

    def update(self, dt):
        self.game.move()
        self.game.usership.move()
        self.game.usership.cooling(0.1)
        self.game.usership.angle = (Vector(Window.mouse_pos) -
                                Vector(Window.width / 2, Window.height / 2)
                                ).angle(Vector(1, 0))
        '''
        for asteroid in self.asteroids:
            asteroid.check_distance()
        '''
        for key in (self.keyboard.key_set | self.mouse.key_set):
            if key in self.settings.keys["Move"]["move_up"]:
                self.game.usership.thrust("forward_t")
                for i in self.game.usership.children:
                    i.color = [1, 1, 1, 1]
            elif key in self.settings.keys["Move"]["move_down"]:
                self.game.usership.thrust("backward_t")
            elif key in self.settings.keys["Move"]["move_left"]:
                self.game.usership.thrust("left_t")
            elif key in self.settings.keys["Move"]["move_right"]:
                self.game.usership.thrust("right_t")
            elif key in self.settings.keys["Combat"]["fire"]:
                # latter there will be bullet type
                self.game.usership.fire()
            elif (key in self.settings.keys["Utils"]["FA"] and
                      not self.settings.keys["Utils"]["FA"][1]
                  ):
                self.settings.FA = not self.settings.FA
                self.settings.keys["Utils"]["FA"][1] = True
                if self.settings.FA:
                    print("Flight assist enabled")
                else:
                    print("Flight assist disabled")
        for bullet in self.bullets:
            bullet.move()
            widgets = []
            for widget in self.game.children:
                if (widget == self.game.skybox_1 or
                    widget == self.game.skybox_2 or
                    widget == self.game.skybox_3 or
                    widget == self.game.skybox_4 or
                    widget == bullet):
                    continue
                widgets.append(widget)
            for widget in widgets:
                if bullet.collide_widget(widget):
                    if widget in self.asteroids:
                        self.bullets.remove(bullet)
                        widget.source = "img/collapse.gif"
                        self.destroy(bullet)
                        Clock.schedule_once(partial(self.destroy, widget), 1.5)
                        Clock.schedule_once(lambda dt: partial(self.asteroids.remove, widget), 1.5)
                    elif widget in self.bots:
                        self.bullets.remove(bullet)
                        widget.source = "img/collapse.gif"
                        self.destroy(bullet)
                        Clock.schedule_once(partial(self.destroy, widget), 1.5)
                        Clock.schedule_once(lambda dt: partial(self.bots.remove, widget), 1.5)

            if (bullet.coords - self.game.usership.coords).length() > Window.height * 2:
                try:
                    self.bullets.remove(bullet)
                    self.destroy(bullet)
                except ValueError:
                    pass
        # For triggers:
        if not self.settings.keys["Utils"]["FA"][0] in self.keyboard.key_set:
            self.settings.keys["Utils"]["FA"][1] = False
        # ------------
        if self.settings.FA and len(self.keyboard.key_set) == 0:
            self.game.usership.flight_assist()
        if len(self.keyboard.del_key_set) != 0:
            self.keyboard.key_set -= self.keyboard.del_key_set
            self.keyboard.del_key_set.clear()
        if len(self.mouse.del_key_set) != 0:
            self.mouse.key_set -= self.mouse.del_key_set
            self.mouse.del_key_set.clear()
    def destroy(self, obj, dt = 0):
        try:
            obj.parent.remove_widget(obj)
        except AttributeError:
            pass
        else:
            del obj
DrawinerApp().run()
