from ursina import *

app = Ursina()
combine_parent = Entity(enabled = False)

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.pink)
e.look_at(Vec3(1, 0, 0), 'up') #right

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.azure)
e.look_at(Vec3(-1, 0, 0), 'up') #left

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.yellow)
e.look_at(Vec3(0, 1, 0), 'up') #top

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.white)
e.look_at(Vec3(0, -1, 0), 'up') #bottom

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.green)
e.look_at(Vec3(0, 0, 1), 'up') #back

e = Entity(parent=combine_parent, model='plane', origin_y =-.5, texture = 'white_cube', color = color.orange)
e.look_at(Vec3(0, 0, -1), 'up') #front

combine_parent.combine()

cubes = []
for x in range(3) :
    for y in range(3) :
        for z in range(3) :
            e = duplicate(combine_parent, position = Vec3(x, y, z) - Vec3(1, 1, 1), texture = 'white_cube')
            cubes.append(e)

collider = Entity(model = 'cube', scale = 3, collider = 'box', visible = False)

def collider_input(key) :
    if mouse.hovered_entity == collider :
        if key == 'left mouse down' :
            rotate(mouse.normal, 1)
        elif key == 'right mouse down' :
            rotate(mouse.normal, -1)

collider.input = collider_input
rotation_helper = Entity()

def rotate(normal, direction=1) :
    for e in cubes :
        if normal == Vec3(1, 0, 0) and e.x > 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_x', 90 * direction, duration = 0.5)
        elif normal == Vec3(-1, 0, 0) and e.x < 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_x', -90 * direction, duration = 0.5)

        if normal == Vec3(0, 1, 0) and e.y > 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_y', 90 * direction, duration = 0.5)
        elif normal == Vec3(0, -1, 0) and e.y < 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_y', -90 * direction, duration = 0.5)

        if normal == Vec3(0, 0, 1) and e.z > 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_z', -90 * direction, duration = 0.5)
        elif normal == Vec3(0, 0, -1) and e.z < 0:
            e.world_parent = rotation_helper
            rotation_helper.animate('rotation_z', 90 * direction, duration = 0.5)

    invoke(reset, delay = 0.55)

def reset() :
    for e in cubes :
        e.world_parent = scene
    rotation_helper.rotation = (0, 0, 0)

EditorCamera()
app.run()
