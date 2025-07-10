from ..constants import get_operator
from ..resources.utils import check_for_textures
def draw_import(context, layout):
    col = layout.column()
    col.scale_y = 2

    if not check_for_textures():
        col.operator(get_operator("import_textures"), icon  = "IMPORT")

    col.operator(get_operator("import_armor"), text = "import Armor", icon  = "IMPORT")
    