import bpy
from ..resources.utils import check_for_textures

class DummyOperator(bpy.types.Operator):
    bl_idname = "object.dummy"
    bl_label = "Dummy"

    def execute(self, context):
        check_for_textures(self)
        return {"FINISHED"}

