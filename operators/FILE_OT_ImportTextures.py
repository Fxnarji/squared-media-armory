import bpy
import zipfile
import os

from ..constants import get_operator, get_addon_root_folder

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

    def import_textures(self,jar_path, addon_root):
        subdirectory = "assets/minecraft/textures/entity/equipment/humanoid"
        with zipfile.ZipFile(jar_path, 'r') as jar:
            for file in jar.namelist():
                if file.startswith(subdirectory):
                    filename = os.path.basename(file)
                    parentdir = os.path.basename(os.path.dirname(file))
                    print(parentdir)
                    output_dir = os.path.join(addon_root, "lib", "textures", parentdir)
                    os.makedirs(output_dir, exist_ok=True)
                    print(f"{output_dir} should be valid now")
                    output_file = os.path.join(output_dir, filename)

                    with jar.open(file) as source, open(output_file, 'wb') as target:
                        target.write(source.read())


    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        self.filepath = self.mc_default_install_dir
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.import_textures(self.filepath, get_addon_root_folder())
        print("Happy")
        return {'FINISHED'}
