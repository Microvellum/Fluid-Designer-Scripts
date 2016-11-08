# This is an example template for Library Assemblies

from mv import fd_types, unit

# Store Assembly references at top of file as constants
DEFAULT_MATERIAL = ("Plastics","White Melamine")

class Material_Pointers():
    
    My_Material_Pointer = fd_types.Material_Pointer(DEFAULT_MATERIAL)

class Cutpart_Pointers():
    
    My_Cutpart_Pointer = fd_types.Cutpart_Pointer(thickness=unit.inch(.75),
                                                  core="My_Material_Pointer",
                                                  top="My_Material_Pointer",
                                                  bottom="My_Material_Pointer")
    
class Edgepart_Pointers():
    
    My_Edgepart_Pointer = fd_types.Edgepart_Pointer(thickness=unit.inch(.01),
                                                    material="My_Material_Pointer")