from direct.showbase.ShowBase import ShowBase
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
#window.exit_button.visible = False
punch = Audio('punch.wav', autoplay=False)

blocks = [
	load_texture('gress.jpg'), #0
	load_texture('ston.png'), #1
	load_texture('wood1.png'), #2
	load_texture('wood2.png'), #3
	load_texture('water.png'), #4
	load_texture('광물.png'), #5
	load_texture('block.png'), #6
	load_texture('leaf.png') #7
]
block_id = 1

def input(key):
	global block_id, hand
	if key.isdigit() :
		block_id = int(key)

		if block_id >= len(blocks) :
			block_id = len(blocks) - 1
			hand.texture = blocks[block_id]

sky = Entity(
	parent=scene,
	model='sphere',
	texture=load_texture('sky.jpg'),
	scale=500,
	double_sided=True
	)

hand = Entity(
	parent=camera.ui,
	model='block',
	texture=blocks[block_id],
	scale=0.2,
	rotation=Vec3(-10, -10, 10),
	position=Vec2(0.6, -0.6)
)

def update():
	if held_keys['left mouse'] or held_keys['right mouse'] :
		punch.play()
		hand.position = Vec2(0.4, -0.5)
	else:
		hand.position = Vec2(0.6, -0.6)

class Voxel(Button) :
	def __init__(self, position=(0, 0, 0), texture='gress.jpg') :
		super().__init__(
			parent=scene,
			position=position,
			model='cube',
			origin_y=0.5,
			texture=texture,
			color=color.color(0, 0, random.uniform(0.9, 1.0)),
			scale=1.0
		)

	def input(self, key) :
		if self.hovered:
			if key == 'right mouse down' :
				Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
			elif key == 'left mouse down' :
				destroy(self)

for z in range(20) :
	for x in range(20):
		voxel = Voxel(position=(x, 0, z))

hand.show
player = FirstPersonController()
app.run()