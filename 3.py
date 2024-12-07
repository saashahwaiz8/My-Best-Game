from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import time
import math

app = Ursina()
Entity.default_shader = lit_with_shadows_shader
sun = DirectionalLight(position = (100,100,100), shadow = True, rotation = (45,0,0))

def update():
    water.x+=0.05
    if water.x>=512:
        water.x=0
    water.y=-5+math.sin(time.monotonic())/4

class Underground(Entity):
    def __init__(self):
        super().__init__(
            model='plane',
            scale=1000,
            collider='box',
            position=(0, -10, 0),
            texture='sand'
        )

class Water(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            scale=(1536, 10, 1536),
            texture='water',
            position=(0, -5, 0),
            collider = 'box'
        )

class Island(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            collider='sphere',
            scale=(20, 4, 30),
            texture='sand',
            position=(0, -1, 0)
        )

class Tree(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            collider='sphere',
            scale=(1, 8, 1),
            texture='wood',
            position=(4, 2, 0)
        )

class Palm(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            collider='sphere',
            scale=(5, 1, 1),
            rotation_y=72,
            texture='grass',
            position=(4, 6, 0)
        )

class Mango(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            color = color.yellow,
            model = 'cube',
            texture = 'white_cube',
            highlight_color = color.lime,
            scale = (0.5,1,0.5),
            collider = 'box',
            position = (3.5,5.5,1.7)
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.position = (3.5,1,1.7)
            if key == "right mouse down":
                self.position = (3.5,1,1.7)

player = FirstPersonController()
Sky()
window.fullscreen = True

Underground()
water = Water()
Island()
Tree()
Palm()
Mango()

player.position = (0, 60, 0)
app.run()
