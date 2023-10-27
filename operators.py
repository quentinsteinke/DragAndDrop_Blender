import bpy
import os

from . import shared_resources as sr
from ctypes import c_char_p


# sr.dll.DragAndDrop.restype = c_char_p
# sr.dll.DragAndDrop.argtypes = []

class DragAndDropImport(bpy.types.Operator):
    bl_idname = "object.drag_and_drop_import"
    bl_label = "Drag and Drop Import"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        results = sr.dll.DragAndDrop()
        results = results.decode("utf-8")
        print(f"From Python: {results}")
        
        # bpy.ops.import_scene.fbx(filepath=self.filepath)
        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(DragAndDropImport.bl_idname, text="import fbx")

registerClasses = [
    DragAndDropImport,
]

def register():
    for cls in registerClasses:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    for cls in registerClasses:
        bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
