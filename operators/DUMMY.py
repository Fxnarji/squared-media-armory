import bpy
import time
from ..resources.utils import check_for_textures

class DummyOperator(bpy.types.Operator):
    bl_idname = "object.dummy"
    bl_label = "Dummy"

    def do_something_with_progress(self):
        wm = bpy.context.window_manager
        total_steps = 10
        
        wm.progress_begin(0, total_steps)
        
        for i in range(total_steps):
            # Simulate work
            time.sleep(0.2)
            print("Helo")
            # Update progress  
            wm.progress_update(i)
        
        wm.progress_end()


    def execute(self, context):
        self.do_something_with_progress()
        return {"FINISHED"}

