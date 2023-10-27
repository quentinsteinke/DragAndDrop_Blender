import ctypes
from ctypes import c_char_p
import os

dll: ctypes.CDLL

def register():
    global dll

    dirName = os.path.dirname(__file__)
    dll = ctypes.CDLL(os.path.join(dirName, "draganddrop.dll"))
    dll.DragAndDrop.restype = c_char_p
    dll.DragAndDrop.argtypes = []
    print(f"Drag and Drop DLL Registered: {dll}")

def unregister():
    global dll

    import _ctypes
    _ctypes.FreeLibrary(dll._handle)