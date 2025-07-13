import bpy
import os

from ..constants import get_addon_root_folder

def check_for_textures(self = None):
    chestplate_path = os.path.join(get_addon_root_folder(), "lib", "textures", "humanoid")
    leggings_path = os.path.join(get_addon_root_folder(), "lib", "textures", "humanoid_leggings")
    
    armor_textures = {
    "chainmail.png": False,
    "leather.png": False,
    "gold.png": False,
    "leather_overlay.png": False,
    "diamond.png": False,
    "iron.png": False,
    "netherite.png": False,
    "turtle_scute.png": False
    }

    
    leggings_textures = {
    "chainmail.png": False,
    "leather.png": False,
    "gold.png": False,
    "leather_overlay.png": False,
    "diamond.png": False,
    "iron.png": False,
    "netherite.png": False,
    }


    total = 0
    missing = 0

    if chestplate_path:
        for filename in os.listdir(chestplate_path):
            if filename in armor_textures:
                armor_textures[filename] = True

    if leggings_path:
        for filename in os.listdir(leggings_path):
            if filename in leggings_textures:
                leggings_textures[filename] = True


    for armor in armor_textures:
        total += 1
        if not armor_textures[armor]:
            missing += 1
            print(f"{armor} missing from Armors!")

    for leggings in leggings_textures:
        total += 1
        if not leggings_textures[leggings]:
            missing += 1
            print(f"{leggings} missing from Leggings!")
    
    if self:
        self.report({'INFO'}, f"Armor Textures: {missing} textures are missing out of {total} textures. Expected are 15 textures.")
    
    if missing == 0:
        return True
    return False

def get_rig(context):
    return bpy.context.active_object

def get_ui_properties(property_name, context):
    property_bone = "WGT_uiProperties"
    rig = get_rig(context)
    pose_bone = rig.pose.bones.get(property_bone)
    return pose_bone
