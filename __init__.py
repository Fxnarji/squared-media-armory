import bpy
from .resources.LoadIcons import load_icons, unload_icons

from .preferences import PF_Preferences

#Operators
from .operators.FILE_OT_ImportTextures        import FILE_OT_ImportTextures
from .operators.FILE_OT_ImportArmor           import FILE_OT_ImportArmor
from .operators.DUMMY                         import DummyOperator

#panels
from .panels.VIEW3D_PT_UI_ArmoryMain        import VIEW3D_PT_UI_ArmoryMain



#reading values such as name, version and more from toml so there is no need to change information in two places
def load_manifest_info():
    from .constants import get_manifest
    manifest = get_manifest()

    #reading addon name
    extension_name = manifest["name"]

    #reading addon version
    version_str = manifest["version"]
    version_tuple = tuple(int(x) for x in version_str.split("."))

    #reading Blender version
    blender_version_str = manifest["blender_version_min"]
    blender_version_tuple = tuple(int(x) for x in blender_version_str.split("."))

    bl_info = {
    "name": extension_name,
    "version": version_tuple, 
    "blender": blender_version_tuple,
    }

    return bl_info

blender_manifest = load_manifest_info()
bl_info = {
    "name": blender_manifest["name"],
    "description": "Adds Armor Support for Minecraft Animatios",
    "author": "Fxnarji",
    "version": blender_manifest["version"], 
    "blender": blender_manifest["blender"],
    "location": "Npanel",
    "support": "COMMUNITY",
    "category": "UI",
}

classes = [
    #preferences
    PF_Preferences,
    #operators:
    FILE_OT_ImportTextures,
    FILE_OT_ImportArmor,
    DummyOperator,

    #panels:
    VIEW3D_PT_UI_ArmoryMain

    ]



def register():
    for i in classes:
        bpy.utils.register_class(i)
    load_icons()

    


def unregister(): 
    unload_icons()
    for i  in reversed(classes):
        bpy.utils.unregister_class(i)

if __name__ == "__main__":
    register() 