import bpy
import zipfile
import os

from ..constants import get_operator, get_addon_root_folder
from ..constants import ArmorProperties

class FILE_OT_ImportTextures(bpy.types.Operator):
    bl_idname = get_operator("import_textures")
    bl_description = "Extract Textures from jar file"
    bl_label = "Imports Textures from Minecraft"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(
        name="Minecraft Version Path",
        subtype="FILE_PATH",
    )#type:ignore

 
    mc_default_install_dir = None
    if os.name == "posix":
        home_dir = os.path.expanduser("~")
        mc_default_install_dir = os.path.join(home_dir, ".minecraft", "versions", "")
    else:
        mc_default_install_dir = ""  # Or another fallback for Windows etc.

    def import_textures(self,jar_path, addon_root, subdirectory, prefix, target_dir = "textures", include_root = True):
        with zipfile.ZipFile(jar_path, 'r') as jar:
            for file in jar.namelist():
                if file.startswith(subdirectory):
                    filename = f"{prefix}_{os.path.basename(file)}"
                    parentdir = os.path.basename(os.path.dirname(file))
                    if include_root:
                        output_dir = os.path.join(addon_root, "lib", target_dir, parentdir)
                    else:
                        output_dir = os.path.join(addon_root, "lib", target_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    print(f"{output_dir} should be valid now")
                    output_file = os.path.join(output_dir, filename)

                    with jar.open(file) as source, open(output_file, 'wb') as target:
                        target.write(source.read())


    def import_textures_and_trims(self):
        armor_chestplate_path = "assets/minecraft/textures/entity/equipment/humanoid/"
        armor_leggings_path = "assets/minecraft/textures/entity/equipment/humanoid_leggings/"
        armor_trim_chest_path = "assets/minecraft/textures/trims/entity/humanoid/"
        armor_trim_leggings_path = "assets/minecraft/textures/trims/entity/humanoid_leggings/"
        armor_palettes_path = "assets/minecraft/textures/trims/color_palettes/"


        self.import_textures(self.filepath, get_addon_root_folder(), subdirectory=armor_chestplate_path,prefix="texture_chest")
        self.import_textures(self.filepath, get_addon_root_folder(), subdirectory=armor_leggings_path,prefix="texture_leggings")
        self.import_textures(self.filepath, get_addon_root_folder(), subdirectory=armor_trim_chest_path,prefix="trim_chest")
        self.import_textures(self.filepath, get_addon_root_folder(), subdirectory=armor_trim_leggings_path,prefix="trim_leggings")
        self.import_textures(self.filepath, get_addon_root_folder(), subdirectory=armor_palettes_path,prefix="palette")

    def import_icons(self):
        directory = "assets/minecraft/textures/item/"
        root = get_addon_root_folder()

        for c in ArmorProperties.colors:
            for t in ArmorProperties.types:
                name = f"{c}_{t}"
                final_directory = directory + name
                print(final_directory)
                self.import_textures(self.filepath, root, subdirectory=final_directory, prefix = "icon", target_dir="icons", include_root= False)


    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        self.filepath = self.mc_default_install_dir
        return {'RUNNING_MODAL'}

    def execute(self, context):
        #self.import_textures_and_trims()
        self.import_icons()
        print("Happy")
        return {'FINISHED'}
