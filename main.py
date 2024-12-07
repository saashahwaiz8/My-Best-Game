from ursina import *
import subprocess

app = Ursina()
wait = "Please wait..."

class Game1(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            color = color.white,
            model = 'cube',
            texture = 'logo_1',
            position = (-5,0),
            scale = (3,3),
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                subprocess.run(['python', '1.py'])
                print(wait)

class Game2(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            color = color.white,
            model = 'cube',
            texture = 'logo_2',
            position = (0,0),
            scale = (3,3),
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                subprocess.run(['python', '2.py'])
                print(wait)

class Game3(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            color = color.white,
            model = 'cube',
            texture = 'logo_3',
            scale = (3,3),
            highlight_color = color.lime,
            position = (5,0,0)
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                subprocess.run(['python', '3.py'])
                print(wait)

Sky(texture = 'sky_sunset')

Game1()
Game2()
Game3()

app.run()
