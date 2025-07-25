import bpy
from .constants import get_operator
from .constants import ArmorProperties
class PF_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        progress = ArmorProperties.progress
        layout = self.layout
        row = layout.row()
        row.scale_y = 2
        operator = get_operator("import_textures")
        row.operator(operator, text = "import textures from Minecraft (.jar file) or Pack (.rar or .zip)")
        layout.progress(text = f"importing: ({progress} / 83 Files done)", type = 'BAR', factor = progress/83)
