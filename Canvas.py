from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Game(Widget):
    main_sky = None
    skybox_1 = ObjectProperty(None)
    skybox_2 = ObjectProperty(None)
    skybox_3 = ObjectProperty(None)
    skybox_4 = ObjectProperty(None)
    usership = ObjectProperty(None)
    skyboxes = []
    last_quarter = None

    def build(self):
        self.usership.bind(on_coords=self.move)

    def get_main_sky(self, found, *args):
        for img in args:
            if ((img.pos[0] <= found.center_x <= img.pos[0] + img.size[0]) and
                    (img.pos[1] <= found.center_y <= img.pos[1] + img.size[1])):
                return img
        return -1

    def get_quarter(self, source, found):
        if ((source.center_x <= found.center_x) and
                (source.center_y <= found.center_y)):
            return 1
        elif ((source.center_x > found.center_x) and
                  (source.center_y <= found.center_y)):
            return 2
        elif ((source.center_x > found.center_x) and
                  (source.center_y > found.center_y)):
            return 3
        elif ((source.center_x <= found.center_x) and
                  (source.center_y > found.center_y)):
            return 4
        else:
            return 1

    def move(self):
        if len(self.skyboxes) == 0:
            self.skyboxes = [self.skybox_1, self.skybox_2, self.skybox_3, self.skybox_4]
        main_sky = self.get_main_sky(self.usership, self.skybox_1,
                                     self.skybox_2, self.skybox_3,
                                     self.skybox_4)
        self.skyboxes.remove(main_sky)
        quarter = self.get_quarter(main_sky, self.usership)
        if quarter != self.last_quarter:
            if quarter == 1:
                self.skyboxes[0].coords.x = main_sky.coords.x
                self.skyboxes[0].coords.y = main_sky.coords.y + main_sky.size[1]

                self.skyboxes[1].coords.x = main_sky.coords.x + main_sky.size[0]
                self.skyboxes[1].coords.y = main_sky.coords.y + main_sky.size[1]

                self.skyboxes[2].coords.x = main_sky.coords.x + main_sky.size[0]
                self.skyboxes[2].coords.y = main_sky.coords.y

            elif quarter == 2:
                self.skyboxes[0].coords.x = main_sky.coords.x - main_sky.size[0]
                self.skyboxes[0].coords.y = main_sky.coords.y

                self.skyboxes[1].coords.x = main_sky.coords.x - main_sky.size[0]
                self.skyboxes[1].coords.y = main_sky.coords.y + main_sky.size[1]

                self.skyboxes[2].coords.x = main_sky.coords.x
                self.skyboxes[2].coords.y = main_sky.coords.y + main_sky.size[1]

            elif quarter == 3:
                self.skyboxes[0].coords.x = main_sky.coords.x - main_sky.size[0]
                self.skyboxes[0].coords.y = main_sky.coords.y

                self.skyboxes[1].coords.x = main_sky.coords.x - main_sky.size[0]
                self.skyboxes[1].coords.y = main_sky.coords.y - main_sky.size[1]

                self.skyboxes[2].coords.x = main_sky.coords.x
                self.skyboxes[2].coords.y = main_sky.coords.y - main_sky.size[1]

            else:
                self.skyboxes[0].coords.x = main_sky.coords.x
                self.skyboxes[0].coords.y = main_sky.coords.y - main_sky.size[1]

                self.skyboxes[1].coords.x = main_sky.coords.x + main_sky.size[0]
                self.skyboxes[1].coords.y = main_sky.coords.y - main_sky.size[1]

                self.skyboxes[2].coords.x = main_sky.coords.x + main_sky.size[0]
                self.skyboxes[2].coords.y = main_sky.coords.y
        self.skyboxes.append(main_sky)
        self.last_quarter = quarter
