import bpy
import os
from ..constants import ArmorProperties, AddonProperties
from ..constants import get_operator, get_addon_root_folder
from ..resources.utils import get_rig

class SHADER_OT_SetTextures(bpy.types.Operator):
    bl_idname = get_operator("settextures")
    bl_label = "SetTexurres"

    material_index: bpy.props.IntProperty()#type:ignore

    Texture: bpy.props.EnumProperty(items = ArmorProperties.colors_enum)

    def get_image_name(self):
        color = self.Texture.lower()
        
        #for some reason minecraft has inconsistencies in their code where its sometimes golden and sometimes gold. F#ck that shit, but we have to deal with it
        if color == "golden":
            color = "gold"
        
        name = f"texture_chest_{color}.png"
        if self.material_index == 2:
            name = f"texture_leggings_{color}.png"
        print(name)
        return name

    def get_texture_path(self):
        root = get_addon_root_folder()
        icons = os.path.join("lib", "textures")

        # 2 = leggings, they have a dedicated texture for some reaons (see opinion above)
        local_path = "humanoid"
        if self.material_index == 2:
            local_path = "humanoid_leggings"

        full_path = os.path.join(root, icons, local_path, self.get_image_name())
        print(full_path)
        return full_path

    def set_texture_in_shader(self, mat_obj, image):
        image_node = mat_obj.material_slots[self.material_index].material.node_tree.nodes["Base"]
        image_node.image = image

    def set_texture_in_GN(self, image, rig):
        property_bone = rig.pose.bones["WGT-UIProperties"]
        property_name = f"{self.material_index}"
        geometry = property_bone[property_name]
        try:
            mod = geometry.modifiers["SQM_GN_ArmorDelete"]
            mod["Socket_2"] = image

            mod.show_viewport = not mod.show_viewport
            mod.show_viewport = not mod.show_viewport
        except:
            print("no modifier found!")

    def import_image_to_file(self,path):
        image_name = self.get_image_name()
        image = bpy.data.images.load(path)
        image.name = image_name

        return image

    def execute(self, context):
        rig = get_rig(context)
        Mat_Obj = rig["Mat_Obj"]
        image = self.import_image_to_file(self.get_texture_path())

        self.set_texture_in_shader(Mat_Obj, image)
        self.set_texture_in_GN(image, rig)


        return {"FINISHED"}

