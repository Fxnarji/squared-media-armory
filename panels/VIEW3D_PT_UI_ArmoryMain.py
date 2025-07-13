import bpy
from ..constants import AddonProperties

from .SUB_Logo      import draw_logo
from .SUB_Import    import draw_import
from .SUB_ArmorPiece    import draw_armor_piece
         
class VIEW3D_PT_UI_ArmoryMain(bpy.types.Panel):
    bl_label = "Squared Media Armory"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = AddonProperties.panel_category


    def draw(self, context):
        layout = self.layout
        draw_logo(context=context, layout=layout)
        #draw_import(context=context, layout=layout)
        draw_armor_piece(context=context, layout=layout, piece="Helmet")
        draw_armor_piece(context=context, layout=layout, piece="Chestplate")
        draw_armor_piece(context=context, layout=layout, piece="Leggings")
        draw_armor_piece(context=context, layout=layout, piece="Boots")
       