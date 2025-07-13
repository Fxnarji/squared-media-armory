#i like to put values i need in multiple places here so i can change them in one place
import os
import tomllib
import bpy

#has to be all lowercase
bl_id_prefix = "sqm_armory" 


class AddonProperties:
    module_name = __package__
    panel_category = "SQM Armory"
    needs_update = False
    remote_version = (0,0,0)

def get_manifest():
    toml_path = os.path.join(os.path.dirname(__file__), "blender_manifest.toml")
    with open(toml_path, "rb") as f:
        manifest = tomllib.load(f)
    return manifest

def get_preferences():
    # No context needed, directly get addon preferences by package name
    addon_prefs = bpy.context.preferences.addons.get(__package__).preferences
    return addon_prefs

def get_operator(name):
    return_string = f"{bl_id_prefix}.{name}"
    return return_string

def get_addon_root_folder():
    return os.path.dirname(__file__)


class ArmorProperties:
    colors = [
        #"leather", 
        #"chainmail",
        "iron", 
        "golden", 
        "diamond", 
        "netherite", 
        ]
    colors_enum = [
        #("LEATHER","leather",""),
        #("CHAINMAIL","chainmail",""),
        ("IRON","iron",""),
        ("GOLDEN","golden",""),
        ("DIAMOND","diamond",""),
        ("NETHERITE","netherite",""),


    ]
    types = ["boots", "chestplate", "helmet", "leggings"]

    progress = 0


 