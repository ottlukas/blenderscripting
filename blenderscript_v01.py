import bpy
import bmesh

def create():
    set_background()    
    #context
    bpyscene = bpy.context.scene

    # Create an empty mesh and the object.
    mesh = bpy.data.meshes.new('Basic_Sphere')
    basic_sphere = bpy.data.objects.new("Basic_Sphere", mesh)

    # Add the object into the scene.
    bpyscene.objects.link(basic_sphere)
    bpyscene.objects.active = basic_sphere
    basic_sphere.select = True

    # Construct the bmesh cube and assign it to the blender mesh.
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
    bm.to_mesh(mesh)
    bm.free()

    # add subsurf mod and smooth
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()

    # add material to the UV Sphere
    ob = bpy.context.active_object

    # Get material
    mat = bpy.data.materials.get("white_glow")
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name="white_glow")

    # Assign it to object
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)
    # move UV Sphere
    bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False))

    # Text
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.object.data.extrude = 0.02
    # Delete default "Text"
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    # Set new word
    chars = "Digital"
    for char in chars:
        bpy.ops.font.text_insert(text=char)
    bpy.ops.object.editmode_toggle()
    # add material to the Text
    ob = bpy.context.active_object

    # Get material
    mat = bpy.data.materials.get("glow")
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name="glow")

    # Assign it to object
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # text to mesh
    bpy.ops.object.convert(target='MESH')
    # Particle system
    bpy.ops.object.particle_system_add()
    bpy.data.particles["ParticleSettings"].effector_weights.gravity = 0
    bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
    bpy.data.particles["ParticleSettings"].dupli_object = bpy.data.objects["Basic_Sphere"]
    
def set_background():
    # darken the background    
    bpy.context.scene.world.node_tree.nodes['Background'].inputs['Color'].default_value = (0, 0, 0, 1)
    print("Set background color")

# Animate Particle System
#def animate():
    
# Move / Animate Sphere

if __name__ == "__main__":
    create()