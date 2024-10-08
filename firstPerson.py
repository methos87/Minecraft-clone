#!usr/bin/env python

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sys import exit


app = Ursina()


grass_texture = load_texture('assets/grass.png')
stone_texture = load_texture('assets/stone.png')
sky_texture = load_texture('assets/sky_texture.png')
#arm_texture = load_texture('assets/arm_texture.png')
block_pick = 1

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['escape']: quit()


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/mcube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            #highlight_color=color.lime,
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
            if key =='right mouse down':
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)


class Hand(Entity):
    def __init__(self):
        super()._init__(
            parent = camera.ui,
            model = 'assets/arm',
            #texture = arm_texture,
            scale = 0.2
            )

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))


player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()

