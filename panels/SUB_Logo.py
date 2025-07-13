from ..resources.LoadIcons import preview_collections

def draw_logo(context, layout):
    box = layout.box()
    pcoll = preview_collections.get("main")
    if pcoll:
        icon_id = pcoll["SQM_Tiny.png"].icon_id
        box.label(text="Squared Media Armory", icon_value=icon_id)

    else:
        box.label(text="Squared Media", icon="RENDER_ANIMATION")
