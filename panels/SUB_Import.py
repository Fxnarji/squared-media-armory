from ..constants import get_operator
def draw_import(context, layout):
    col = layout.column()
    col.scale_y = 2
    col.operator(get_operator("import_textures"), icon  = "IMPORT")
    col.operator(get_operator("import_armor"), icon  = "IMPORT")
    