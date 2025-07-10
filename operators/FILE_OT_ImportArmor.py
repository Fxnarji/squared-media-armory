import bpy
import os
from ..constants import get_operator, get_addon_root_folder


class FILE_OT_ImportArmor(bpy.types.Operator):
    bl_idname = get_operator("import_armor")
    bl_description = "Import Armor into the scene"
    bl_label = "Imports Armor from the addon"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        armor_path = os.path.join(get_addon_root_folder(), "lib", "blendfiles", "SQM-Armory.blend")
        armor_collection = "SQM-Armor"
        print(f"importing from {armor_path}")
        bpy.ops.wm.append(
                filepath=armor_path, 
                directory=armor_path + "/Collection/",  
                filename=armor_collection,
            )
        return {'FINISHED'}
