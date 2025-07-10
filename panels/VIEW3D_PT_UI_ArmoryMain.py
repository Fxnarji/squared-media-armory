import bpy
from ..constants import AddonProperties
from ..constants import get_operator
from .SUB_Logo import draw_logo
         
class VIEW3D_PT_UI_ArmoryMain(bpy.types.Panel):
    bl_label = "Squared Media Armory"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = AddonProperties.panel_category


    def draw(self, context):
       layout = self.layout
       draw_logo(context=context, layout=layout)