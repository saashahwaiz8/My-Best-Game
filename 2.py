from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

class Ground1(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            scale = Vec3(10,1,10),
            texture = 'grass',
            collider = 'box'
        )

class Wall1(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(.5,2,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall2(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(2.5,3.5,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall3(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(4.5,5.5,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall4(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(6.5,7.5,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall5(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(8.5,9.5,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall6(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(10.5,11.5,1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall7(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,1-1.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall8(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,-3.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall9(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,-6.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall10(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,-9.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall11(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,-11.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall12(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(1.5,.5,1.5),
            position = Vec3(11.5,11.5,-14.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Wall13(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(13.5,1,13.5),
            position = Vec3(11.5,-20.5,-23.5),
            collider = 'box',
            shader = basic_lighting_shader
        )

class Respawn_Side(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            scale = Vec3(60,5,60),
            position = Vec3(11.5,-1000,-35.5),
            color = color.green,
            collider = 'box'
        )

class Earth(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model ='sphere',
            scale = Vec3(40),
            texture = 'sky_default',
            position = Vec3(11.5,-30,-25.5),
            double_sided = True
        )

class Ground2(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            scale = Vec3(11.5,1,11.5),
            position = Vec3(17.5,-34,-17.5),
            texture = 'grass'
        )

app = Ursina()
Sky(texture = 'sky_sunset')
window.fullscreen = True # If you want to check it here, cut the command!
player = FirstPersonController(model = 'cube', texture = 'white_cube', shader = basic_lighting_shader)
camera.z = -5

Ground1()
Wall1()
Wall2()
Wall3()
Wall4()
Wall5()
Wall6()
Wall7()
Wall8()
Wall9()
Wall10()
Wall11()
Wall12()
Wall13()
Earth()
Ground2()
respawn_side = Respawn_Side()

app.run()
# Code by @Programmer P #
