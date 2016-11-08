from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Edgepart(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def mv_pointer_name(self):
        '''(String)'''
        return str()
    @property
    def thickness(self):
        '''(Float)'''
        return float()
    @property
    def material(self):
        '''(String)'''
        return str()