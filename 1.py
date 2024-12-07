from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

app = Ursina()

def update():
    if held_keys['tab']:
        camera.z = -5
    if held_keys['control']:
        camera.z = 0

class Voxel(Button):
    def __init__(self,position=(0,0,0)):
        super().__init__(
            parent = scene,
            color = color.white,
            model = 'cube',
            texture = 'stone',
            collider = 'box',
            shader = basic_lighting_shader,
            highlight_color = color.lime,
            position = position
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)

for x in range(11):
    for y in range(11):
        for z in range(11):
            voxel = Voxel(position=(x,y,z))

class Cow(Entity):
    def __init__(self):
        super().__init__(
            model = 'cow',
            texture = 'Image_0_2',
            scale = (1,1,1),
            position = (5,10.7,8)
        )

player = FirstPersonController(model = 'cube', texture = 'white_cube', shader = basic_lighting_shader)
Sky(texture = 'castaway_sky')
window.fullscreen = True

cow = Cow()

player.position = (0,20,0)
app.run()
