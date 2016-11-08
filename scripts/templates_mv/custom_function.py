# This is an example template for defining a custom python function
import bpy
from mv import unit
from bpy.app.handlers import persistent

def MV_CLOSET_PANEL_PRICE(depth):
    if depth <= unit.inch(12):
        return 195
    elif depth <= unit.inch(14):
        return 215
    elif depth <= unit.inch(16):
        return 235
    elif depth <= unit.inch(20):
        return 275
    elif depth <= unit.inch(24):
        return 315
    elif depth <= unit.inch(32):
        return 380
    elif depth <= unit.inch(36):
        return 470
    elif depth <= unit.inch(48):
        return 510
    else:
        return 1000000

@persistent
def load_driver_functions(scene=None):
    bpy.app.driver_namespace["MV_CLOSET_PANEL_PRICE"] = MV_CLOSET_PANEL_PRICE
    
bpy.app.handlers.load_post.append(load_driver_functions)