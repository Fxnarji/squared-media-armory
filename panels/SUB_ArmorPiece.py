import bpy
from ..resources.utils import get_rig
from ..constants import get_operator
from ..resources.LoadIcons import preview_collections
from ..constants import ArmorProperties


def draw_armor_piece(context, layout, piece: str):
    armor_piece_box = layout.box()
    rig = get_rig(context)
   
    property_bone = "WGT-UIProperties"

    armor_piece_box.prop(rig.pose.bones[property_bone],f'["{piece}"]', toggle = True, icon = "DOWNARROW_HLT" if rig.pose.bones[property_bone][piece] else "RIGHTARROW", emboss = False, text = piece)
    pcoll = preview_collections.get("main")

    if rig.pose.bones[property_bone][piece]:


        # -- Texture  --
        armor_piece_box.column().label(text="Texture:")
        base = armor_piece_box.row(align = True)
        base.scale_y = 2
        base.scale_x = 2

        material_index_map = {
            "Helmet": 0,
            "Chestplate": 1,
            "Leggings": 2,
            "Boots": 3
        }

        for c in ArmorProperties.colors:
            if pcoll:
                icon_name = f"icon_{c.lower()}_{piece.lower()}.png"
                icon_id = pcoll[icon_name].icon_id
                set_texture = base.operator(get_operator("settextures"), text="", icon_value=icon_id)
                set_texture.Texture = c.upper()
                set_texture.material_index = material_index_map.get(piece, -1)


                