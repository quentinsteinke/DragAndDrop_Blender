bl_info = {
    "name": "Drag and Drop FBX Importer",
    "version": (1, 0),
    "blender": (3, 6, 5),
    "category": "Import-Export",
}

import bpy
import ctypes
import os
import importlib

if "shared_resources" in locals():
    importlib.reload(shared_resources)
else:
    from . import shared_resources

if "operators" in locals():
    importlib.reload(operators)
else:
    from . import operators

def register():
    shared_resources.register()
    operators.register()


def unregister():
    shared_resources.unregister()
    operators.unregister()