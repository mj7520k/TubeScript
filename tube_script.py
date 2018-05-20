import bpy

VERTICES = 10

DEPTH = 1

INSIDE_DIAMETER = 1
OUTSIDE_DIAMETER = 2

def delete(obj):
    name = obj.name
    bpy.context.scene.objects.unlink(bpy.context.scene.objects[name])
    bpy.data.objects.remove(bpy.data.objects[name])
    bpy.data.meshes.remove(bpy.data.meshes[name])
    if name in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials[name])

def main():
    if INSIDE_DIAMETER > OUTSIDE_DIAMETER:
        return
    bpy.ops.mesh.primitive_cylinder_add(vertices = VERTICES, depth = DEPTH + 1, radius = INSIDE_DIAMETER)
    INSIDE = bpy.context.object
    bpy.ops.mesh.primitive_cylinder_add(vertices = VERTICES, depth = DEPTH, radius = OUTSIDE_DIAMETER)
    OUTSIDE = bpy.context.object
    
    boolean = OUTSIDE.modifiers.new("Boolean", "BOOLEAN")
    boolean.object = INSIDE
    boolean.operation = "DIFFERENCE"
    bpy.ops.object.modifier_apply(apply_as="DATA", modifier="Boolean")
    
    delete(INSIDE)

if __name__ == "__main__":
    main()